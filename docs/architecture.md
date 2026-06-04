# AI Cloud Security Architects Platform — Architecture

## System Architecture Diagram
┌─────────────────────────────────────────────────────────────┐
│                        GitHub                                │
│                                                              │
│   ┌─────────────────┐    OIDC Token    ┌─────────────────┐  │
│   │  GitHub Actions │ ──────────────► │ Workload Identity│  │
│   │  CI/CD Pipeline │                 │ Federation (GCP) │  │
│   └────────┬────────┘                 └─────────────────┘  │
└────────────┼────────────────────────────────────────────────┘
│ Deploy
▼
┌─────────────────────────────────────────────────────────────┐
│                    GCP Project: cis410-delphin               │
│                                                              │
│   ┌──────────────────────────────────────────────────────┐  │
│   │                    VPC Network                        │  │
│   │                                                       │  │
│   │   ┌─────────────┐      ┌──────────────────────────┐  │  │
│   │   │  Cloud Run  │─────►│     Cloud SQL            │  │  │
│   │   │  (Flask App)│      │  (PostgreSQL Database)   │  │  │
│   │   └──────┬──────┘      └──────────────────────────┘  │  │
│   │          │                                            │  │
│   └──────────┼────────────────────────────────────────── ┘  │
│              │                                               │
│   ┌──────────▼──────────┐  ┌──────────────────────────────┐ │
│   │  Artifact Registry  │  │      Secret Manager          │ │
│   │  (Docker Images)    │  │  (DB Password, API Keys)     │ │
│   └─────────────────────┘  └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
## Components

| Component | Purpose |
|---|---|
| **Cloud Run** | Hosts the Flask security dashboard (serverless containers) |
| **Cloud SQL (PostgreSQL)** | Stores threat data, alerts, and compliance reports |
| **VPC Network** | Isolates resources in private network (10.0.0.0/24) |
| **Secret Manager** | Stores DB password and sensitive credentials |
| **Artifact Registry** | Stores Docker images for the Flask app |
| **OIDC / Workload Identity** | Passwordless auth between GitHub Actions and GCP |

## CI/CD Flow

1. Developer pushes code to `main` branch
2. GitHub Actions triggers `terraform-plan.yml`
3. OIDC exchanges GitHub token for GCP credentials
4. Terraform plans infrastructure changes
5. Docker image built and pushed to Artifact Registry
6. Cloud Run deploys new container revision
