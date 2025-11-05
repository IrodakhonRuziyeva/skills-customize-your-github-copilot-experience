from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# TODO: Create TaskModel class with required fields

# TODO: Initialize FastAPI application

# TODO: Implement CRUD endpoints:
# - POST /tasks
# - GET /tasks
# - GET /tasks/{task_id}
# - PUT /tasks/{task_id}
# - DELETE /tasks/{task_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)