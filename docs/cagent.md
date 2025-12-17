# cagent

## Description

cagent is a powerful, customizable multi-agent runtime developed by Docker that orchestrates AI agents with specialized capabilities and tools, managing interactions between agents in a hierarchical architecture.

## Primary Objective

Provide a production-ready runtime for creating, deploying, and running multi-agent AI systems with easy-to-configure agents that can collaborate using external tools and delegate tasks to specialized sub-agents.

## Core Capabilities

### Agent Management
- Multi-agent orchestration with hierarchical agent structures
- YAML-based declarative agent configuration
- Agent delegation via built-in `transfer_task` tool
- Agent distribution through OCI registry (Docker Hub) with push/pull commands
- Interactive agent generation using `cagent new` command

### Tool Integration
- **MCP (Model Context Protocol) support**:
  - stdio transport for local MCP servers
  - HTTP and SSE transports for remote MCP servers
  - Docker MCP Gateway integration for containerized tools
  - Tool filtering and whitelisting per agent
- **Built-in tools**:
  - `think`: Step-by-step reasoning
  - `todo`: Task list management
  - `memory`: Persistent SQLite-based storage
  - `filesystem`: File operations
  - `shell`: Command execution
  - `script`: Custom shell scripts
  - `fetch`: HTTP requests

### AI Provider Support
- OpenAI (GPT models)
- Anthropic (Claude models)
- Google Gemini
- xAI
- Mistral
- Nebius
- Docker Model Runner (DMR) for local inference with llama.cpp/vLLM

### RAG (Retrieval-Augmented Generation)
- Multiple retrieval strategies:
  - BM25 (keyword-based search)
  - Chunked-embeddings (vector similarity)
  - Semantic-embeddings (full-document embeddings)
- Hybrid retrieval with result fusion (Reciprocal Rank Fusion, weighted, max score)
- Result reranking with specialized models
- Automatic file watching and reindexing
- Configurable chunking strategies

### Execution & Runtime
- Event-driven streaming architecture with buffered channels
- Non-blocking tool execution with confirmation flow
- Session management with conversation history
- Context-aware message limiting via `num_history_items`
- Max iterations control to prevent infinite loops
- OpenTelemetry tracing support

### Interfaces
- Terminal User Interface (TUI) using Bubble Tea
- Command-Line Interface (CLI)
- REST/SSE API server
- MCP server mode (expose agents as MCP tools)
- A2A (Agent-to-Agent) protocol server

### Evaluation & Testing
- Agent evaluation framework
- VCR-based testing for deterministic AI API interactions
- Golden file pattern for snapshot testing

## Technical Architecture

### Runtime Flow
1. Tool discovery from agent configuration
2. Message preparation with session history
3. LLM streaming with real-time chunk processing
4. Tool execution with optional user confirmation
5. Iterative loop until completion or max iterations reached

### Event System
- Buffered event channels (capacity 128)
- Event types: StreamStarted, AgentChoice, ToolCall, ToolCallConfirmation, ToolCallResponse, ErrorEvent, StreamStopped
- Multiple event consumers: TUI, CLI, API server, MCP gateway

### Configuration System
- Version-based config schema (currently v2)
- Sequential migration support (v0 → v1 → v2)
- Dynamic environment variable gathering
- Model references support inline or defined models

## Key Components

- **Agent System** (`pkg/agent/`): Core agent abstraction with name, description, instruction, toolsets, models, and sub-agents
- **Runtime System** (`pkg/runtime/`): Event-driven execution engine with tool coordination
- **Tools** (`pkg/tools/`): Built-in tools and MCP protocol implementations
- **Model Providers** (`pkg/model/provider/`): AI provider integrations
- **Configuration** (`pkg/config/`): YAML parsing, validation, and versioning
- **Gateway** (`pkg/gateway/`): MCP server implementation
- **A2A** (`pkg/a2a/`): Agent-to-Agent protocol implementation
- **RAG** (`pkg/rag/`): Retrieval strategies, chunking, fusion, and reranking
- **Telemetry** (`pkg/telemetry/`): Anonymous usage tracking

## Protocols & Standards

- **MCP (Model Context Protocol)**: Tool discovery, invocation, and resource access via stdio, HTTP, and SSE transports
- **A2A (Agent-to-Agent)**: Standard protocol for agent communication and task delegation
- **OCI (Open Container Initiative)**: Agent packaging and distribution via container registries
- **OpenTelemetry**: Distributed tracing for runtime operations and tool calls

## Programming Languages

- **Primary**: Go (runtime, agent system, tools, configuration)
- **Supporting**: Python (MCP server examples), Shell scripts (build automation)

## Repository

https://github.com/docker/cagent

