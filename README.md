# Trade Backend API

A simple backend REST API for handling trade orders, built with **FastAPI**, **PostgreSQL**, and deployed on **AWS EC2** with **Docker** and **CI/CD via GitHub Actions**.

---

## **Features**

- Accepts trade orders (symbol, price, quantity, order type)
- List all submitted trade orders
- CI/CD pipeline with GitHub Actions
- Deployed on AWS EC2 using Docker

---

##**Tech Stack**

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Cloud:** AWS EC2

---

##**API Endpoints**

| Method | Endpoint      | Description               |
|--------|---------------|---------------------------|
| `POST` | `/orders`     | Submit a new trade order  |
| `GET`  | `/orders`     | Get all trade orders      |
| `GET`  | `/docs`       | Swagger UI Documentation  |

---
📖 API Documentation (Swagger/OpenAPI)

The API is self-documented using Swagger UI.
	•	Swagger UI (API Docs):
http://localhost:8000/docs (for local development)
http://3.144.37.210:8000/docs (when deployed on EC2)

##**Running Locally**

### 1**Clone the Repository**

```bash
git clone https://github.com/smishra291/trade-backend.git
cd trade-backend