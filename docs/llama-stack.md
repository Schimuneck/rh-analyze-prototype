# Llama Stack

## Description

Llama Stack is Meta's standardized framework that defines and implements the core building blocks needed to develop and deploy generative AI applications using Llama models, providing a unified API layer with a rich ecosystem of provider implementations.

## Primary Objective

Simplify AI application development by providing a unified set of APIs with multiple provider implementations, enabling developers to build applications once and deploy them flexibly across different infrastructure environments (local, cloud, on-premises, mobile) without changing code.

## Core Capabilities

### Unified API Layer
- **Inference**: Chat completions, embeddings, text generation
- **RAG (Retrieval-Augmented Generation)**: Vector storage and retrieval
- **Agents**: Multi-step reasoning and tool-calling agents
- **Tools**: Function calling and external integrations
- **Safety**: Content moderation with Llama Guard
- **Evals**: Model evaluation and benchmarking
- **Post-Training**: Fine-tuning and distillation
- **DatasetIO**: Dataset loading and management

### Plugin Architecture
- 25+ API provider implementations
- Pluggable infrastructure for each API component
- Mix-and-match providers per deployment
- External provider packages support

### Pre-Packaged Distributions
- **Starter**: Basic setup with Ollama + ChromaDB
- **Starter-GPU**: GPU-enabled local inference
- **Meta Reference GPU**: Meta's reference implementation
- **PostgreSQL Demo**: Vector storage with PG Vector
- **Dell**: Dell-optimized distribution
- **NVIDIA**: NVIDIA infrastructure integration
- **OCI**: Oracle Cloud Infrastructure
- **WatsonX**: IBM WatsonX integration
- **Open Benchmark**: Evaluation-focused distribution

### Multi-Provider Inference
- **Hosted providers**:
  - SambaNova
  - Cerebras
  - Fireworks
  - AWS Bedrock
  - Together
  - Groq
  - NVIDIA NIM
  - OpenAI
  - Anthropic
  - Gemini
  - WatsonX
- **Self-hosted/Local**:
  - Ollama
  - TGI (Text Generation Inference)
  - vLLM
  - PyTorch ExecuTorch (on-device iOS)
  - Meta Reference (native implementation)

### Vector Storage Providers
- **Hosted/Self-hosted**:
  - ChromaDB
  - Milvus
  - Qdrant
  - Weaviate
- **Local**:
  - SQLite-vec
  - PG Vector (PostgreSQL)

### Safety Integration
- Llama Guard integration for content filtering
- Moderation via AWS Bedrock, SambaNova, Together, NVIDIA NIM
- Configurable safety policies

### Post-Training Capabilities
- **HuggingFace**: Dataset integration
- **TorchTune**: Fine-tuning framework
- **NVIDIA NEMO**: Enterprise-grade training and evaluation

### Developer Interfaces
- **CLI**: `llama` command for server management and model operations
- **Client CLI**: `llama-stack-client` for distribution queries
- **Python SDK**: `llama-stack-client` package
- **Swift SDK**: iOS/macOS native integration
- **TypeScript SDK**: Node.js and browser support
- **Kotlin SDK**: Android and JVM integration

### On-Device Support
- **PyTorch ExecuTorch**: Mobile deployment for iOS
- Agents API on-device
- Inference API on-device

## Technical Architecture

### Distribution Model
Distributions bundle provider implementations for specific deployment scenarios:

```
Distribution = {
  Inference Provider: (e.g., Ollama),
  VectorIO Provider: (e.g., ChromaDB),
  Safety Provider: (e.g., Meta Reference),
  Agents Provider: (e.g., Meta Reference),
  ...
}
```

### Stack Components

1. **Core APIs** (`llama_stack_api/`): API definitions and schemas
2. **Providers** (`llama_stack/providers/`):
   - `inline/`: Local/embedded providers
   - `remote/`: Remote service providers
   - `registry/`: Provider registration
3. **Models** (`llama_stack/models/`): Llama model implementations
4. **Distributions** (`llama_stack/distributions/`): Pre-configured bundles
5. **CLI** (`llama_stack/cli/`): Command-line interface
6. **Server** (`llama_stack/core/server/`): HTTP server implementation
7. **UI** (`llama_stack_ui/`): Next.js-based web interface

### Storage Abstraction
- **KVStore**: Key-value storage interface
- **SQLStore**: SQL database abstraction
- Implementations for various backends

### Router System
- Request routing to appropriate providers
- Routing tables for API endpoint mapping
- Multi-provider orchestration

## Key Components

### Core Library (`llama_stack/`)
- API implementations and routing
- Provider management
- Distribution configuration
- Server startup and lifecycle

### API Package (`llama_stack_api/`)
- API schemas and type definitions
- FastAPI route definitions
- Common data types and errors
- OpenAPI specifications

### Models (`llama_stack/models/llama/`)
- Llama model implementations (65 Python files)
- Tokenization
- Model configuration
- Inference logic

### Providers (`llama_stack/providers/`)
- **Inline providers** (139 files): Local implementations
- **Remote providers** (139 files): API client implementations
- **Registry** (12 files): Provider discovery and registration
- **Utils** (38 files): Shared provider utilities

### UI (`llama_stack_ui/`)
- Next.js/React web application (148 TypeScript files)
- Chat playground
- Prompt management
- Log viewing
- File management
- Vector store visualization

### Client SDKs
Maintained in separate repositories:
- `llama-stack-client-python`
- `llama-stack-client-swift`
- `llama-stack-client-typescript`
- `llama-stack-client-kotlin`

## Protocols & Standards

- **REST API**: HTTP-based API for all operations
- **OpenAI-compatible endpoints**: Compatible chat completion API
- **Streaming**: Server-Sent Events (SSE) for real-time responses
- **Agent Protocol**: Multi-step agent interactions
- **MCP (Model Context Protocol)**: Tool integration (compatibility layer)

## Programming Languages

- **Python**: Core framework, providers, API server (541+ files)
- **TypeScript/React**: Web UI (148 files)
- **Swift**: iOS SDK
- **Kotlin**: Android/JVM SDK
- **JavaScript**: Node.js SDK

## Deployment Environments

### Single Node
- Local development with Ollama
- Meta Reference GPU for production
- vLLM for high-performance inference

### Hosted Cloud
- Provider-managed infrastructure
- Multi-cloud support (AWS, GCP, Azure via providers)
- Managed service integrations

### On-Device
- iOS via PyTorch ExecuTorch
- Mobile-optimized models
- Offline inference capability

## Installation & Setup

### One-Line Installer
```bash
curl -LsSf https://github.com/llamastack/llama-stack/raw/main/scripts/install.sh | bash
```

### Manual Installation
```bash
pip install llama_stack
llama stack list-deps <distribution> | xargs pip install
llama stack run <distribution>
```

### Docker Distributions
Available on Docker Hub:
- `llamastack/distribution-starter`
- `llamastack/distribution-meta-reference-gpu`
- `llamastack/distribution-postgres-demo`

## Configuration Management
- YAML-based distribution configuration
- Environment variable support
- Provider-specific settings
- Model configuration files

## Testing & Development
- API recorder for test generation
- Integration tests (GitHub Actions)
- Unit tests across all components
- E2E tests for UI

## Repository

https://github.com/llamastack/llama-stack

## Related Repositories

- https://github.com/meta-llama/llama-stack-client-python
- https://github.com/meta-llama/llama-stack-client-swift
- https://github.com/meta-llama/llama-stack-client-typescript
- https://github.com/meta-llama/llama-stack-client-kotlin
- https://github.com/meta-llama/llama-stack-apps (Example applications)

## Documentation

https://llamastack.github.io/docs

