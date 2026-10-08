from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class NewTask(BaseModel):
    title: str

class UpdateTask(BaseModel):
    title: str
    done: bool

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
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def add_task(new_task: NewTask):
    task = {"id": len(tasks) + 1, "title": new_task.title, "done": False}
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: UpdateTask):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated.title
            task["done"] = updated.done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")