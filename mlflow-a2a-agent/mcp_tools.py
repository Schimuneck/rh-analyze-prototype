"""
Dynamic MCP Tool Registration

Creates ClientTool wrappers for MCP servers defined in MCP_SERVERS_JSON.
Supports environment variable substitution in headers for secure token injection.
"""
import os
import json
import re
import logging
from typing import Any, Dict, List, Optional
from functools import partial

import httpx
from llama_stack_client.lib.agents.client_tool import ClientTool, client_tool
from llama_stack_client.lib.agents.types import CompletionMessage, ToolResponse

logger = logging.getLogger(__name__)


def substitute_env_vars(value: str) -> str:
    """Replace ${VAR_NAME} with environment variable values."""
    def replace(match):
        var_name = match.group(1)
        return os.getenv(var_name, "")
    return re.sub(r'\$\{(\w+)\}', replace, value)


def load_mcp_config() -> List[Dict[str, Any]]:
    """Load MCP server configuration with environment variable substitution."""
    config_str = os.getenv("MCP_SERVERS_JSON", "[]")
    
    # Substitute environment variables in the entire JSON string
    config_str = substitute_env_vars(config_str)
    
    try:
        config = json.loads(config_str)
        logger.info(f"Loaded {len(config)} MCP server configurations")
        return config
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse MCP_SERVERS_JSON: {e}")
        return []


def discover_mcp_tools(server_config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Discover available tools from an MCP server.
    
    Calls the tools/list method to get tool definitions.
    """
    url = server_config["url"]
    headers = server_config.get("headers", {})
    
    # Substitute env vars in headers
    headers = {k: substitute_env_vars(v) for k, v in headers.items()}
    
    try:
        # MCP tools/list request
        response = httpx.post(
            url,
            json={
                "jsonrpc": "2.0",
                "method": "tools/list",
                "id": 1
            },
            headers=headers,
            timeout=30.0
        )
        response.raise_for_status()
        result = response.json()
        
        if "result" in result and "tools" in result["result"]:
            tools = result["result"]["tools"]
            logger.info(f"Discovered {len(tools)} tools from {server_config['name']}")
            return tools
        else:
            logger.warning(f"No tools found in response from {server_config['name']}")
            return []
            
    except Exception as e:
        logger.error(f"Failed to discover tools from {server_config['name']}: {e}")
        return []


def call_mcp_tool(
    server_config: Dict[str, Any],
    tool_name: str,
    arguments: Dict[str, Any]
) -> Any:
    """
    Call an MCP tool and return the result.
    """
    url = server_config["url"]
    headers = server_config.get("headers", {})
    
    # Substitute env vars in headers
    headers = {k: substitute_env_vars(v) for k, v in headers.items()}
    
    try:
        response = httpx.post(
            url,
            json={
                "jsonrpc": "2.0",
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": arguments
                },
                "id": 1
            },
            headers=headers,
            timeout=60.0
        )
        response.raise_for_status()
        result = response.json()
        
        if "result" in result:
            content = result["result"].get("content", [])
            # Extract text content from MCP response
            if isinstance(content, list):
                texts = [c.get("text", str(c)) for c in content if isinstance(c, dict)]
                return "\n".join(texts) if texts else str(content)
            return str(content)
        elif "error" in result:
            return f"Error: {result['error'].get('message', 'Unknown error')}"
        else:
            return str(result)
            
    except Exception as e:
        logger.error(f"Failed to call MCP tool {tool_name}: {e}")
        return f"Error calling tool: {e}"


class MCPClientTool(ClientTool):
    """
    A ClientTool that wraps an MCP tool.
    """
    
    def __init__(
        self,
        server_config: Dict[str, Any],
        tool_definition: Dict[str, Any]
    ):
        self.server_config = server_config
        self.tool_definition = tool_definition
        self._name = f"{server_config['name']}_{tool_definition['name']}"
        self._description = tool_definition.get("description", "")
        self._parameters = tool_definition.get("inputSchema", {})
    
    def get_name(self) -> str:
        return self._name
    
    def get_description(self) -> str:
        return self._description
    
    def get_params_definition(self) -> Dict[str, Any]:
        return self._parameters
    
    def get_tool_definition(self) -> Dict[str, Any]:
        """Return tool definition in OpenAI function format."""
        return {
            "type": "function",
            "function": {
                "name": self._name,
                "description": self._description,
                "parameters": self._parameters
            }
        }
    
    def run(self, messages: List[CompletionMessage]) -> ToolResponse:
        """Execute the MCP tool call."""
        # Extract arguments from the last message's tool call
        if not messages:
            return ToolResponse(
                call_id="unknown",
                tool_name=self._name,
                content="No messages provided",
                metadata={}
            )
        
        last_message = messages[-1]
        if not last_message.tool_calls:
            return ToolResponse(
                call_id="unknown",
                tool_name=self._name,
                content="No tool calls in message",
                metadata={}
            )
        
        tool_call = last_message.tool_calls[0]
        
        # Parse arguments
        arguments = tool_call.arguments
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError:
                arguments = {}
        
        # Call the actual MCP tool
        result = call_mcp_tool(
            self.server_config,
            self.tool_definition["name"],
            arguments
        )
        
        return ToolResponse(
            call_id=tool_call.call_id,
            tool_name=self._name,
            content=result,
            metadata={"mcp_server": self.server_config["name"]}
        )
    
    async def async_run(self, messages: List[CompletionMessage]) -> ToolResponse:
        """Async version - just calls sync for now."""
        return self.run(messages)


def create_mcp_client_tools() -> List[ClientTool]:
    """
    Create ClientTools for each MCP server/tool combination.
    
    Returns a list of ClientTool instances that can be passed to the Agent.
    """
    tools: List[ClientTool] = []
    
    for server_config in load_mcp_config():
        server_name = server_config.get("name", "unknown")
        tool_whitelist = server_config.get("tools", [])
        
        logger.info(f"Processing MCP server: {server_name}")
        
        # Discover available tools
        mcp_tools = discover_mcp_tools(server_config)
        
        for tool_def in mcp_tools:
            tool_name = tool_def.get("name", "")
            
            # Filter by whitelist if specified
            if tool_whitelist and tool_name not in tool_whitelist:
                logger.debug(f"Skipping tool {tool_name} (not in whitelist)")
                continue
            
            # Create ClientTool wrapper
            client_tool = MCPClientTool(server_config, tool_def)
            tools.append(client_tool)
            logger.info(f"Registered tool: {client_tool.get_name()}")
    
    logger.info(f"Total MCP tools registered: {len(tools)}")
    return tools


# For testing
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Test with sample config
    os.environ["MCP_SERVERS_JSON"] = json.dumps([
        {
            "name": "test",
            "url": "http://localhost:8080/mcp",
            "tools": ["test_tool"]
        }
    ])
    
    tools = create_mcp_client_tools()
    print(f"Created {len(tools)} tools")

