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

Initialize with your chosen language (Node.js or Python).

Set up endpoints for CRUD operations.

Connect to a database (like PostgreSQL or DynamoDB).

Add authentication and business logic.


## Summary of Why Each Step Matters
```
### Step	                                             ### purpose 

Install Docker & Docker Compose                          	Isolate environments, run services locally and consistently

Set up AWS CLI & CDK	                                     Prepare to deploy infrastructure as code to AWS

Choose Backend Language	                                  Create and manage APIs that serve your app

Choose Frontend Framework	                                Build an interactive, user-friendly web interface

Initialize Repositories                                  	Organize code cleanly and support scalable development
```
