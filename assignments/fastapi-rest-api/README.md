# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a RESTful API using the FastAPI framework to build a simple task management system. This assignment will help you understand API development, HTTP methods, data validation, and documentation.

## 📝 Tasks

### 🛠️ Setup and Basic API Structure

#### Description
Set up a FastAPI project and create the basic API structure with proper routing and data models.

#### Requirements
Completed program should:

- Initialize a FastAPI application with proper project structure
- Create a Pydantic model for Task items (id, title, description, status)
- Implement basic error handling and response models
- Set up API documentation using FastAPI's built-in Swagger UI

### 🛠️ Implement CRUD Operations

#### Description
Create endpoints to handle basic CRUD (Create, Read, Update, Delete) operations for tasks.

#### Requirements
Completed program should:

- Implement POST /tasks endpoint to create new tasks
- Create GET /tasks endpoint to list all tasks
- Add GET /tasks/{task_id} endpoint to retrieve a specific task
- Implement PUT /tasks/{task_id} endpoint to update tasks
- Create DELETE /tasks/{task_id} endpoint to remove tasks
- Include proper input validation for all endpoints