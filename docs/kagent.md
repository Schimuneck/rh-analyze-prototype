# kagent

## Description

kagent is a Kubernetes-native framework for building AI agents that integrates seamlessly with Kubernetes infrastructure, providing a declarative and observable way to deploy, manage, and run AI agents at scale.

## Primary Objective

Make Kubernetes the orchestration platform for AI agents by providing a flexible, extensible, and observable framework that works with any agent implementation and leverages Kubernetes-native patterns for deployment and lifecycle management.

## Core Capabilities

### Kubernetes Integration
- Custom Resource Definitions (CRDs) for Agent and ToolServer resources
- Kubernetes controller for agent lifecycle management
- Declarative YAML-based agent and tool definitions
- Helm charts for deployment and configuration
- Multi-namespace support for team isolation
- PostgreSQL and SQLite storage backends

### Agent Execution
- **ADK (Agent Development Kit)** engine powered by Google's ADK for agent execution
- Framework-agnostic design supporting any agent implementation
- Agent execution in Kubernetes pods
- RESTful API for agent interactions

### LLM Provider Support
- OpenAI
- Azure OpenAI
- Anthropic
- Google Vertex AI
- Ollama (local models)
- Custom providers via AI gateways

### Tool Integration
- **MCP (Model Context Protocol)** tools as Kubernetes resources
- Pre-built MCP tools for infrastructure:
  - Kubernetes operations
  - Istio service mesh
  - Helm package management
  - Argo workflows
  - Prometheus metrics
  - Grafana dashboards
  - Cilium networking
- ToolServer CRD for tool registration and discovery

### Observability
- OpenTelemetry tracing for agent and tool interactions
- Integration with monitoring frameworks
- Real-time agent status tracking
- Tool execution visibility

### Management Interfaces
- **Web UI**: React/TypeScript-based management interface
- **CLI**: Command-line tool for agent operations (`kagent` CLI)
- **Helm**: Declarative deployment via Helm charts

### Development & Testing
- Local development with Kind (Kubernetes in Docker)
- Debug mode with localhost agent connections
- Comprehensive test suite

## Technical Architecture

### Core Components

1. **Controller** (Go): Kubernetes controller watching Agent and ToolServer CRDs, creating necessary resources
2. **Engine** (Python): Executes agents using Google's Agent Development Kit (ADK)
3. **UI** (TypeScript/React): Web interface for agent and tool management
4. **CLI** (Go): Command-line tool for operations

### Architecture Layers

```
┌─────────────────────────────────┐
│         User/Developer          │
└────────┬────────────────────────┘
         │
    ┌────┴────┬────────┬──────┐
    │         │        │      │
   CLI       UI      API   Helm
    │         │        │      │
    └────┬────┴────┬───┴──────┘
         │         │
    ┌────┴─────────┴────┐
    │  Controller (CRDs) │
    └────────┬───────────┘
             │
    ┌────────┴───────────┐
    │  Engine (ADK)      │
    │  - Agent Execution │
    │  - Tool Calling    │
    └────────┬───────────┘
             │
    ┌────────┴───────────┐
    │   Kubernetes       │
    │   - Pods           │
    │   - Services       │
    │   - Storage        │
    └────────────────────┘
```

## Key Components

### Go Components (`go/`)
- Kubernetes controller for CRD reconciliation
- CLI implementation
- API server
- Storage backends (PostgreSQL, SQLite)

### Python Components (`python/`)
- ADK engine integration
- Agent execution runtime
- Tool invocation logic

### UI Components (`ui/`)
- React/TypeScript web application
- Agent management interface
- Tool configuration
- Real-time status monitoring

### Helm Charts (`helm/`)
- kagent deployment charts
- Dependency management
- Configuration templates

### Tools & Addons (`contrib/`)
- Pre-built MCP tool definitions
- Kubernetes-specific tools
- Infrastructure integration tools

## Protocols & Standards

- **Kubernetes API**: Native CRD-based resource management
- **MCP (Model Context Protocol)**: Tool discovery and invocation standard
- **OpenTelemetry**: Distributed tracing protocol for observability
- **Helm**: Package management and deployment
- **A2A (Agent-to-Agent)**: Agent communication protocol (via ADK)

## Programming Languages

- **Go**: Controller, CLI, API server, storage backends
- **Python**: ADK engine, agent runtime
- **TypeScript/React**: Web UI
- **YAML**: Configuration and resource definitions

## Project Status

- Cloud Native Computing Foundation (CNCF) project
- Active development with community contributions
- OpenSSF Best Practices compliant

## Repository

https://github.com/kagent-dev/kagent

