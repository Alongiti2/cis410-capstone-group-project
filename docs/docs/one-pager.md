# AI Cloud Security Architects LLC — Company One-Pager

## 1. Company Name
AI Cloud Security Architects LLC

## 2. Team Roles
| Name | Role | GitHub |
|---|---|---|
| Delphin Alongiti Zaki | Project Lead / DevSecOps Engineer | Alongiti2 |
| Blessing Zaki | Backend Engineer | TBD |
| Rebecca Zaki | Frontend Engineer | TBD |
| John Zaki | DevSecOps Engineer | TBD |
| James Zaki & Jovial Zaki | Security Reviewers | TBD |

## 3. App Overview
AI Cloud Security Architects Platform is a web application with a REST API and security dashboard providing automated threat detection, vulnerability scanning, compliance monitoring, and centralized cloud security reporting.

## 4. Tech Stack
- **Backend:** Python Flask
- **Database:** PostgreSQL (Cloud SQL)
- **Container:** Docker
- **Registry:** Google Artifact Registry
- **Hosting:** Google Cloud Run
- **IaC:** Terraform
- **CI/CD:** GitHub Actions
- **Security:** OIDC, Secret Manager, Workload Identity Federation

## 5. Architecture Sketch
See docs/architecture.md for full diagram.
- GitHub Actions → OIDC → GCP
- Cloud Run (Flask) → Cloud SQL (PostgreSQL)
- Artifact Registry → Cloud Run
- Secret Manager → Cloud Run

## 6. CI/CD Plan
- Push to main triggers terraform-plan.yml
- OIDC authenticates GitHub Actions to GCP
- Terraform validates infrastructure
- Docker image built and pushed to Artifact Registry
- Cloud Run deploys latest image

## 7. Milestones
| Week | Milestone |
|---|---|
| Week 9 | Company setup, repo creation, one-pager |
| Week 10 | Architecture, Terraform structure, OIDC |
| Week 11 | Flask app, Docker, full deployment, demo |

## 8. Security Commitments
- Passwordless authentication via OIDC/Workload Identity Federation
- All secrets stored in GCP Secret Manager (no hardcoded credentials)
- Private VPC network for database isolation
- Least-privilege IAM roles for service accounts
- Container security scanning in CI/CD pipeline

## 9. Signatures
- Delphin Alongiti Zaki — Project Lead
- Blessing Zaki — Backend Engineer
- Rebecca Zaki — Frontend Engineer
- John Zaki — DevSecOps Engineer
- James Zaki — Security Reviewer
- Jovial Zaki — Security Reviewer
