from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NewTask(BaseModel):
    title: str

tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build Task API", "done": False},
]

@app.get("/")
def home():
    return {"message": "hello"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}

@app.post("/tasks")
def add_task(new_task: NewTask):
    task = {"id": len(tasks) + 1, "title": new_task.title, "done": False}
    tasks.append(task)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}