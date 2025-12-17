# kagenti

## Description

Kagenti is a cloud-native middleware platform that provides framework-neutral, scalable, and secure infrastructure for deploying and orchestrating AI agents through standardized REST APIs in production Kubernetes environments.

## Primary Objective

Bridge the gap between agent development frameworks and production deployment by providing standardized infrastructure services—authentication, authorization, deployment, scaling, discovery, and persistence—that work with any agent framework.

## Core Capabilities

### Framework-Neutral Agent Platform
- Supports multiple agent frameworks:
  - LangGraph
  - CrewAI
  - AG2 (AutoGen)
  - Llama Stack
  - BeeAI
  - Any framework implementing A2A protocol
- Framework-agnostic deployment model
- Standardized REST API regardless of underlying framework

### Agent Lifecycle Management
- **Agent Lifecycle Operator**: Kubernetes admission webhook for agent deployment
- Build agents from source code using Tekton pipelines
- Container image management
- Automated lifecycle coordination (updates, rollbacks, scaling)
- Multi-namespace tenant isolation (team1, team2, etc.)

### Identity & Authorization (Auth Bridge)
- **SPIRE (Workload Identity)**:
  - SPIFFE-based cryptographic workload identities
  - SVID (SPIFFE Verifiable Identity Document) issuance
  - CSI driver for certificate mounting
  - Node-level attestation agents
- **Keycloak (Access Management)**:
  - OAuth/OIDC authentication flows
  - User and client management
  - Token exchange for delegated authorization
  - SSO across platform components
- **Authorization Pattern**:
  - Replace static credentials with dynamic tokens
  - Short-lived, scope-limited access tokens
  - Continuous authentication
  - Least privilege enforcement

### MCP Gateway
- **Envoy-based gateway** for Model Context Protocol tool routing
- Unified entry point for MCP servers and tools
- Automatic tool discovery and registration
- Authentication and policy enforcement
- Load balancing across tool replicas
- **MCP Broker Controller**: Manages MCPServer custom resources
- HTTPRoute and Gateway API integration

### Service Mesh Integration
- **Istio Ambient** (sidecar-free service mesh):
  - Zero-config mTLS between services
  - Ztunnel for node-local proxying and traffic interception
  - Waypoint proxies for L7 processing and egress gateway policies
  - HBONE protocol for secure overlay network
- Traffic management and routing
- Security policy enforcement

### Deployment Infrastructure
- Kubernetes-native architecture
- Helm charts for component deployment
- Ansible-based installer for automated setup
- Support for Kind (local), OpenShift, and standard Kubernetes
- Container registry integration
- Metrics server for resource monitoring

### Management & Observability
- **Kagenti UI** (Streamlit-based):
  - Import A2A agents from Git repositories
  - Deploy MCP tools from source
  - Interactive agent testing via chat interface
  - Monitoring dashboards
- **Phoenix**: LLM observability and tracing
- **Kiali**: Service mesh visualization and topology
- Keycloak admin interface
- SPIRE Tornjak UI for identity management

### Configuration & Secrets
- Environment variable management
- Kubernetes ConfigMaps and Secrets integration
- OAuth secret injection via automated jobs

## Technical Architecture

### System Components

```
kagenti-system namespace:
├── Kagenti UI (Streamlit)
├── Agent Lifecycle Operator (Webhook)
├── Ingress Gateway
└── Kiali (observability)

gateway-system namespace:
└── MCP Gateway (Envoy)

mcp-system namespace:
├── MCP Broker Controller
└── MCP Broker Router

keycloak namespace:
└── Keycloak Server + PostgreSQL

Workload namespaces (team1, team2, ...):
├── A2A Agents (LangGraph, CrewAI, AG2, etc.)
├── MCP Tools (weather, slack, fetch, etc.)
└── Custom workloads

Infrastructure services:
├── SPIRE (Identity)
├── Istio Ambient (Service Mesh)
└── Tekton (Build Pipelines)
```

### Data Flow

1. **North-South traffic**: External requests → Ingress Gateway → Agents
2. **East-West traffic**: Inter-service communication → Istio Ambient → Ztunnel → Services
3. **Tool access**: Agent → MCP Gateway → MCP Tool
4. **Identity flow**: SPIRE → Keycloak token exchange → Delegated access

## Key Components

### Kagenti UI (`kagenti/ui/`)
- Streamlit-based Python application
- Pages: Home, Agents, Tools, Admin, Traces
- Agent import from Git URLs
- Tool deployment from source
- Interactive chat testing
- Phoenix integration for traces

### Agent Lifecycle Operator
- Admission webhook for agent builds
- Tekton pipeline orchestration
- AgentBuild and AgentCard CRDs
- Source-to-container automation

### MCP Gateway (`mcp-gateway` repository)
- Go-based Envoy control plane
- HTTPRoute-based tool routing
- MCPServer CRD management
- Tool prefix namespacing

### Identity & Auth Bridge (`kagenti/auth/`)
- Agent OAuth secret generation
- UI OAuth secret generation
- Client registration automation
- Demo setup scripts for GitHub and Slack

### Helm Charts (`charts/`)
- `kagenti`: Main platform components
- `kagenti-deps`: Infrastructure dependencies (Keycloak, SPIRE, Istio, cert-manager)
- `gateway-api`: Kubernetes Gateway API CRDs

### Ansible Deployment (`deployments/ansible/`)
- Automated installer playbook
- Kind cluster configuration
- Image preloading
- Environment value templates

## Protocols & Standards

- **A2A (Agent-to-Agent)**: Google's protocol for agent communication and discovery
- **MCP (Model Context Protocol)**: Anthropic's protocol for tool/server integration
- **SPIFFE/SPIRE**: Workload identity standard with SVID certificates
- **OAuth 2.0 / OIDC**: Authentication and authorization flows
- **Istio Ambient**: Sidecar-free service mesh architecture
- **Kubernetes Gateway API**: Modern ingress and routing standard

## Programming Languages

- **Python**: UI (Streamlit), installer, demos, auth automation
- **Go**: MCP Gateway, operator components
- **YAML**: Configuration, Helm templates, Kubernetes manifests
- **Shell**: Installation scripts, automation

## Infrastructure Requirements

- Python ≥3.9 with uv package manager
- Docker Desktop, Rancher Desktop, or Podman (16GB RAM, 4 cores)
- Kind, kubectl, Helm for Kubernetes
- Ollama for local LLM inference (optional)

## Repository

https://github.com/kagenti/kagenti

## Related Repositories

- https://github.com/kagenti/kagenti-operator (Agent lifecycle operator)
- https://github.com/kagenti/mcp-gateway (MCP Gateway)
- https://github.com/kagenti/kagenti-extensions (Extensions and plugins)
- https://github.com/kagenti/agent-examples (Sample agents and tools)
- https://github.com/kagenti/agentic-control-plane (A2A agent control plane)

