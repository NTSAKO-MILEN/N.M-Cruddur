
# Phase 1 — App Containerization 

Welcome to my phase 1 journey of containerizing a full-stack application using Docker. As someone transitioning into cloud security with a background in biomedical sciences, this is part of my hands-on learning aligned with [Andrew Brown's AWS Bootcamp](https://github.com/andrewbrown/aws-bootcamp-cruddur-2023). I'm documenting everything in a clear, beginner-friendly way for myself and others who are new to DevOps, containers, or full-stack projects.

---

## 🔍 References

### Debugging "Connection Refused" in Docker  
A very helpful article if your app can't talk to other services:  
👉 https://pythonspeed.com/articles/docker-connection-refused/

---

## ⚙️ VSCode Docker Extension

VSCode’s Docker extension simplifies container management:  
👉 https://code.visualstudio.com/docs/containers/overview  
✅ Pre-installed in Gitpod — no setup needed!

---

## 🐍 Containerizing the Backend (Flask + Python)

### ▶️ Run Flask Without Docker (First Step)

```sh
cd backend-flask
export FRONTEND_URL="*"
export BACKEND_URL="*"
python3 -m flask run --host=0.0.0.0 --port=4567
```

- Open port 4567 in Gitpod
- Visit the browser URL and go to `/api/activities/home`
- You should see JSON response

---

### 🐳 Add a Dockerfile for Flask

Create this file: `backend-flask/Dockerfile`

```dockerfile
FROM python:3.10-slim-buster

WORKDIR /backend-flask
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENV FLASK_ENV=development
EXPOSE ${PORT}
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567" ]
```

---

### 🏗️ Build the Backend Image

```sh
docker build -t backend-flask ./backend-flask
```

---

### 🚀 Run the Backend Container

Basic run:
```sh
docker run --rm -p 4567:4567 -it backend-flask
```

With environment variables:
```sh
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
```

Run in background and get container ID:
```sh
CONTAINER_ID=$(docker run --rm -p 4567:4567 -d backend-flask)
```

---

### 🧪 Test with curl

```sh
curl -X GET http://localhost:4567/api/activities/home -H "Accept: application/json"
```

---

### 📝 Logs and Debugging

```sh
docker logs $CONTAINER_ID -f
docker exec -it $CONTAINER_ID /bin/bash
```

Bonus: Use `busybox` for deep debugging:
```sh
docker run --rm -it busybox
```

---

## 🎨 Containerizing the Frontend (React.js)

### 📦 Install NPM Dependencies

```sh
cd frontend-react-js
npm install
```

---

### 🐳 Add Dockerfile for React

Create this file: `frontend-react-js/Dockerfile`

```dockerfile
FROM node:16.18

ENV PORT=3000
COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
```

---

### 🏗️ Build and Run the Frontend

```sh
docker build -t frontend-react-js ./frontend-react-js
docker run -p 3000:3000 -d frontend-react-js
```

---

## 🧱 Multiple Containers with docker-compose

Create a file at root: `docker-compose.yml`

```yaml
version: "3.8"
services:
  backend-flask:
    build: ./backend-flask
    ports:
      - "4567:4567"
    volumes:
      - ./backend-flask:/backend-flask
    environment:
      FRONTEND_URL: "https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
      BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"

  frontend-react-js:
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"

networks:
  internal-network:
    driver: bridge
    name: cruddur
```

---

## 💾 Add Databases for Future Use

### 🐘 Postgres (Coming Soon)

```yaml
services:
  db:
    image: postgres:13-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - '5432:5432'
    volumes:
      - db:/var/lib/postgresql/data
volumes:
  db:
    driver: local
```

Install Postgres client in Gitpod:
```sh
sudo apt update
sudo apt install -y postgresql-client-13 libpq-dev
```

---

### ☁️ DynamoDB Local

```yaml
services:
  dynamodb-local:
    user: root
    image: amazon/dynamodb-local:latest
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal
```

Example Repo:  
👉 https://github.com/100DaysOfCloud/challenge-dynamodb-local

---

## 📦 Volumes Summary

**Named volume:**
```yaml
volumes:
  db:
    driver: local
```

**Directory mapping:**
```yaml
volumes:
  - "./docker/dynamodb:/home/dynamodblocal/data"
```

---

## ✨ About This Project

This containerization journey is part of my AWS and cloud security learning path. I'm aiming to deeply understand how cloud-native apps are developed, deployed, and debugged — from Docker to DevOps — while building a portfolio that reflects my progress and commitment to hands-on learning.
