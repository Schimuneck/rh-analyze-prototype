# MLflow

## Description

MLflow is an open-source platform for managing the complete machine learning and AI lifecycle, from experimentation and training to deployment and monitoring, with comprehensive support for both traditional ML and modern LLM/GenAI applications.

## Primary Objective

Provide an integrated platform that enables data scientists and AI developers to build, track, evaluate, and deploy ML models and AI applications with confidence through end-to-end observability, experiment tracking, and lifecycle management.

## Core Capabilities

### LLM / GenAI Features

#### Tracing & Observability
- **Auto-tracing** for major GenAI libraries:
  - OpenAI
  - LangChain
  - LlamaIndex
  - DSPy
  - AutoGen (AG2)
  - Anthropic
  - Gemini
  - Bedrock
  - CrewAI
  - Haystack
  - Semantic Kernel
  - Pydantic AI
  - Smolagents
- Automatic trace capture via `mlflow.{library}.autolog()`
- Manual instrumentation support
- Trace visualization in web UI
- Distributed trace correlation

#### LLM Evaluation
- **Built-in scorers**:
  - Correctness (LLM judge)
  - Guidelines (custom criteria LLM judge)
  - Toxicity detection
  - Answer relevance
  - Faithfulness
  - Context precision/recall
- Custom scorer development
- Batch evaluation with `mlflow.genai.evaluate()`
- Comparison across multiple model versions
- Integration with experiment tracking

#### Prompt Management
- Version control for prompts
- Centralized prompt registry
- Prompt templates with variables
- Reuse across organization
- Lineage tracking

#### Application Version Tracking
- Track models, prompts, tools, and code together
- End-to-end lineage for AI applications
- Version comparison
- Reproducibility guarantees

### Traditional ML Features

#### Experiment Tracking
- **Autologging** for ML frameworks:
  - scikit-learn
  - TensorFlow
  - PyTorch
  - Keras
  - XGBoost
  - LightGBM
  - CatBoost
  - Spark MLlib
  - H2O
  - Statsmodels
  - Prophet
  - Pmdarima
  - ONNX
  - Paddle
  - Spacy
- Manual logging of parameters, metrics, and artifacts
- Hierarchical run organization
- Tag-based filtering
- Interactive comparison UI

#### Model Registry
- Centralized model store
- Model versioning with stages (None, Staging, Production, Archived)
- Collaborative model management
- Model aliases for flexible referencing
- Model lineage and metadata
- Access control integration

#### Model Deployment
- **Deployment targets**:
  - Local inference server
  - Docker containers
  - Kubernetes
  - Azure ML
  - AWS SageMaker
  - Databricks
  - Custom deployment plugins
- Batch and real-time scoring
- Model serving with REST API
- OpenAI-compatible endpoints for LLMs

### Data Management
- **Dataset tracking** with multiple sources:
  - Pandas DataFrames
  - NumPy arrays
  - Spark DataFrames
  - TensorFlow datasets
  - Delta Lake tables
  - Hugging Face datasets
  - UC Volume datasets
  - Filesystem datasets
  - HTTP datasets
- Dataset versioning
- Dataset registry
- Schema tracking

### System Integration
- **Model flavors** for framework-specific serialization
- **Projects** for packaging ML code with dependencies
- **Plugins** for extensibility
- **Gateway** for unified inference API with multiple providers

## Technical Architecture

### Core Components

1. **Tracking Server**: Backend for logging runs, parameters, metrics, and artifacts
2. **Model Registry**: Centralized model repository with versioning
3. **UI Server**: Interactive web interface for visualization
4. **Client SDK**: Python/TypeScript/Java/R libraries for API interaction
5. **Deployment Services**: Model serving infrastructure
6. **Gateway**: Unified inference routing layer

### Storage Backends
- **Metadata**: SQLite (local), PostgreSQL, MySQL, MSSQL
- **Artifacts**: Local filesystem, S3, Azure Blob, GCS, SFTP, NFS, HDFS
- **Model Registry**: Database-backed with artifact store

### API Layers
- **Python SDK**: Primary interface with `mlflow` package
- **REST API**: HTTP endpoints for all operations
- **CLI**: Command-line tools (`mlflow server`, `mlflow run`, `mlflow models serve`)

## Key Components

### Tracking (`mlflow/tracking/`)
- Run management and logging
- Metric and parameter storage
- Artifact upload/download
- Autologging implementations

### Models (`mlflow/models/`)
- Model serialization (pickle, HDF5, ONNX, etc.)
- Flavor-specific loaders
- Model signature inference
- Dependency management

### GenAI (`mlflow/genai/`)
- Evaluation framework
- Judges and scorers
- Labeling utilities
- Optimization tools
- Git-based versioning

### Tracing (`mlflow/tracing/`)
- Span creation and management
- Auto-instrumentation hooks
- Trace export and storage
- Correlation ID management

### Server (`mlflow/server/`)
- TypeScript/React web UI (1,180 .tsx files)
- REST API backend
- Authentication integration
- Visualization components

### Deployments (`mlflow/deployments/`)
- Deployment plugin system
- Provider implementations (Databricks, OpenAI, etc.)
- Local serving infrastructure

### Gateway (`mlflow/gateway/`)
- Provider registry
- Request routing
- Schema validation
- Rate limiting
- Credential management

## Protocols & Standards

- **MLflow Tracking Protocol**: REST API for experiment tracking
- **MLflow Model Format**: Standardized model packaging (MLmodel file, conda.yaml, requirements.txt)
- **OpenAPI**: REST API specification
- **OpenTelemetry**: Trace instrumentation (partial support)
- **OpenAI API**: Compatible endpoints for LLM serving

## Programming Languages

- **Python**: Primary SDK, core functionality, server backend
- **TypeScript/React**: Web UI (1,180 .tsx files, 303 .ts files)
- **JavaScript**: UI components and utilities
- **Java**: Client SDK and Spark integration
- **R**: Client SDK
- **Scala**: Spark integration

## Hosting Options

MLflow can be self-hosted or used as a managed service:

### Managed Services
- **Amazon SageMaker**: AWS-hosted MLflow
- **Azure ML**: Microsoft-hosted MLflow
- **Databricks**: Enterprise MLflow with enhanced features
- **Nebius**: Cloud-hosted MLflow

### Self-Hosted
- Local development (SQLite + local filesystem)
- On-premises servers (PostgreSQL/MySQL + network storage)
- Cloud infrastructure (containerized deployments)

## Multi-Language Support

- **Python**: `pip install mlflow`
- **TypeScript/JavaScript**: `npm install mlflow-tracing`
- **Java**: Maven artifact `org.mlflow:mlflow-client`
- **R**: CRAN package `mlflow`

## Integration Ecosystem

Native integrations with 20+ frameworks including:
- **Deep Learning**: TensorFlow, PyTorch, Keras, Paddle
- **Traditional ML**: scikit-learn, XGBoost, LightGBM, CatBoost
- **LLM/GenAI**: OpenAI, LangChain, LlamaIndex, DSPy, AutoGen, CrewAI
- **Distributed**: Spark MLlib, H2O
- **Specialized**: Prophet, Statsmodels, Pmdarima, Spacy, ONNX

## Repository

https://github.com/mlflow/mlflow

## Website

https://mlflow.org

