📚 Book Catalog API

A Django REST Framework–based API for managing a catalog of books, integrated with a CI/CD pipeline using GitHub Actions, containerized with Docker, and deployable on Kubernetes (via K3d) with GitOps workflow automation using Argo CD.

🚀 Features

RESTful CRUD API for managing books.

Endpoints for health checks and test responses.

Automated testing with Pytest.

CI/CD pipeline with GitHub Actions.

Containerization with Docker.

Kubernetes deployment via Helm.

GitOps continuous delivery with Argo CD.

🛠 Tech Stack

Django, Django REST Framework, Pytest, PostgreSQL, Docker, Kubernetes (K3d), Argo CD, GitHub Actions.

📂 Project Structure

api/ (models, views, serializers, tests), bookcatalog/ (settings), envs/prod/values.yaml (Helm values), requirements.txt, Dockerfile, docker-compose.yml, entrypoint.sh, README.md.

⚙️ Installation & Local Setup

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

🐳 Running with Docker

docker-compose up --build

Access at http://localhost:8000/api/books/

🔗 API Endpoints

GET /api/books/ – List all books, POST /api/books/ – Create book, GET /api/books/{id}/ – Retrieve book, PUT /api/books/{id}/ – Update book, DELETE /api/books/{id}/ – Delete book, GET /api/health/ – Health check, GET /api/test/ – Test endpoint.

🧪 Running Tests

pytest

Or:

python manage.py test

⚡ CI/CD Pipeline

Runs tests, validates migrations, performs semantic release, builds and pushes Docker image to GHCR, updates Helm values for deployment.

☸️ Kubernetes Deployment (K3d)

k3d cluster create devops
helm upgrade --install books-catalog-api ./charts/books-catalog-api

Argo CD automatically syncs changes.


👤 Author

@cctsbs24059