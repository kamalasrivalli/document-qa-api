# Document Q&A API

A containerized REST API built with FastAPI and PostgreSQL, deployed to AWS EC2 with an automated CI/CD workflow using GitHub Actions and AWS Systems Manager (SSM).

## Architecture

- **FastAPI:** Exposes REST endpoints for document operations.
- **PostgreSQL:** Stores document records.
- **Docker & Docker Compose:** Containerize and run the API and database.
- **AWS EC2:** Hosts the application on Ubuntu.
- **AWS Systems Manager:** Executes deployment commands remotely without requiring GitHub Actions to SSH into the server.
- **GitHub Actions:** Triggers automated deployments when changes are pushed to the `main` branch.
- **Docker named volume:** Persists PostgreSQL data across database container recreation.

## Deployment workflow

1. Push a code change to the `main` branch on GitHub.
2. GitHub Actions authenticates to AWS.
3. AWS Systems Manager sends a deployment command to the EC2 instance.
4. The instance pulls the latest code.
5. Docker Compose rebuilds and restarts the API container.
6. GitHub Actions reports the remote command's status and output.

## API endpoints

- `GET /` — Health-check message.
- `GET /docs` — Interactive Swagger API documentation.
- `GET /documents` — Retrieve document records.
- `POST /documents` — Create a document record.

## Run locally

Requirements: Python, Docker, and Docker Compose.

```bash
git clone https://github.com/kamalasrivalli/document-qa-api.git
cd document-qa-api
docker compose up -d --build
```

Open `http://localhost:8000/docs` to explore the API.

## Key learning outcomes

- Building REST endpoints with FastAPI.
- Connecting an API to PostgreSQL using environment-based configuration.
- Running multi-container applications with Docker Compose.
- Deploying an application to AWS EC2.
- Using IAM permissions and AWS Systems Manager for remote deployment.
- Automating deployments with GitHub Actions.
- Persisting database data using Docker named volumes.

## Security notes

This is a learning project. Before production use, configure HTTPS, review public API access, protect database credentials, and replace long-lived AWS access keys with short-lived credentials through GitHub OIDC.
