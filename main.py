from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []


class Task(BaseModel):
    title: str
    done: bool = False


@app.get("/")
def home():
    return {"message": "Task API is running"}


@app.post("/tasks")
def create_task(task: Task):
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {"id": new_id, "title": task.title, "done": task.done}
    tasks.append(new_task)
    return new_task


@app.get("/tasks")
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")