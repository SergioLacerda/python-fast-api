# 🚀 FastAPI Project Example

This is a sample **FastAPI project** with a clean structure using **routes → controller → service** layers and unit tests.

- Requires **Python 3.9+**

---

## ⚙️ Setup

### 1. Clone repository
```bash
git clone https://github.com/your-username/fastapi_project.git
cd fastapi_project
```

### 2. Create virtual environment
```bash
python -m venv venv
```

Activate it:

- Linux / Mac:
  ```bash
  source venv/bin/activate
  ```
- Windows:
  ```bash
  venv\Scripts\activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Server will start at:
```

```

## ⚙️ Run with Docker

### 1. Build Docker image
```bash
docker build -t fastapi-project .
```

### 2. Run container
```bash
docker run -d -p 8000:8000 fastapi-project
```

---

### Example Endpoints
- Health check → [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)  
- Get all clients → [http://127.0.0.1:8000/clients](http://127.0.0.1:8000/clients)  
- Get client by ID → [http://127.0.0.1:8000/clients/1](http://127.0.0.1:8000/clients/1)  

---

### Interactive API Docs
- Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## ⚙️ Run Unit Tests

We use **pytest** for unit tests.

```bash
pytest -v
```
