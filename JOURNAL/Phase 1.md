# Phase 1: Set Up the Development Environment

## Tools

### -Docker & Docker Compose

**What it does:** Packages your application and all its dependencies into containers.

**Why:** Ensures consistency across different environments (development, testing, production). you can easily run the app on any machine with Docker installed, without worrying about dependencies or OS differences.

**Docker Compose:** Lets you define multi-container applications (e.g., backend + frontend + database) using a single docker-compose.yml file.


### -AWS CLI & CDK (or Terraform)

#### AWS CLI:

**What it does:** Command-line interface for interacting with AWS services.

**Why:** Needed to deploy infrastructure, upload files to S3, interact with Lambda, etc.

#### AWS CDK (Cloud Development Kit):

**What it does:** Lets you define cloud infrastructure using code (in TypeScript, Python, etc.).

**Why:** It’s easier and more repeatable than using the AWS console manually.

**Alternative:** Terraform — another Infrastructure as Code (IaC) tool; use one or the other based on your preference.


 ### -Node.js or Python for backend

**Why:** CRUDder needs an API server to handle requests (create, read, update, delete posts, etc.).

**Node.js** (e.g., with Express.js): Great for real-time or JavaScript-heavy apps.

**Python** (e.g., with FastAPI or Flask): Ideal if you're more comfortable with Python and want fast development with rich features.


### -React or Vue for frontend
**Why:** To build a dynamic single-page application (SPA) where users can create and interact with posts.

**React:** Popular, flexible, and heavily used in industry.

**Vue:** Easier learning curve, especially good for beginners.


### Initialize Repositories:

**cruddur-frontend** AND **cruddur-backend**

**Why:** Separate codebase for the backend logic and APIs.

**What i will do**:

-- Initialize with your chosen language (Node.js or Python).

-- Set up endpoints for CRUD operations.

-- Connect to a database (like PostgreSQL or DynamoDB).

-- Add authentication and business logic.


## Summary of Why Each Step Matters
```
### Step	                                             ### purpose 

Install Docker & Docker Compose                          	Isolate environments, run services locally and consistently

Set up AWS CLI & CDK	                                     Prepare to deploy infrastructure as code to AWS

Choose Backend Language	                                  Create and manage APIs that serve your app

Choose Frontend Framework	                                Build an interactive, user-friendly web interface

Initialize Repositories                                  	Organize code cleanly and support scalable development
```

#### NB- For this project, I will be working with GitPod. GitPod operates in a cloud-based Linux container with tools either preinstalled or easily installable via the Dockerfile or initialization script.

### Step 1: Organize Project Folder
##### Organization of our monorepo 
```
cruddur/
├── backend/
│   └── (Node.js or Python API code)
├── frontend/
│   └── (React or Vue app)
├── .gitpod.yml
├── .gitpod.Dockerfile
├── docker-compose.yml
└── README.md
```

## 📁 .gitpod.yml
Tells Gitpod how to initialize and start your project:
```
image:
  file: .gitpod.Dockerfile

tasks:
  - name: Install & Start
    init: |
      cd backend && npm install || pip install -r requirements.txt
      cd ../frontend && npm install
    command: |
      docker-compose up
```
## 📁 .gitpod.Dockerfile
Installs Docker, AWS CLI, CDK, Node.js, and Python tools:
```
FROM gitpod/workspace-full

# Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Python
RUN apt-get install -y python3 python3-pip

# AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && sudo ./aws/install

# AWS CDK
RUN npm install -g aws-cdk

# Docker & Compose
RUN apt-get update && apt-get install -y docker.io docker-compose
```

## 📁 docker-compose.yml
Sample config to run frontend and backend together:
```
version: "3.8"
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    volumes:
      - ./backend:/app
    command: npm start # or python app.py

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
    command: npm run dev
```
| N.B Make sure you add Dockerfile and package.json or requirements.txt to both frontend/ and backend/.

### ✅ Step 2: Push to GitHub and Launch in Gitpod

# Push your repo to GitHub.
Open it in Gitpod via:
```
bash
Copy
Edit
https://gitpod.io/#https://github.com/your-username/cruddur
```


