# Task API

A simple REST API for managing tasks, built with Python and FastAPI.

## Features

- Create a task
- List all tasks
- Get a single task by id
- Delete a task
- Automatic interactive API docs at `/docs`

## Tech Stack

Python 3.11, FastAPI, Uvicorn, Pydantic

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| POST | `/tasks` | Create a task |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{task_id}` | Get one task (404 if not found) |
| DELETE | `/tasks/{task_id}` | Delete a task (404 if not found) |

## Run Locally

```bash
git clone https://github.com/04imam/task-api.git
cd task-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs to try the API in your browser.

## Example Request

`POST /tasks`

```json
{
  "title": "Learn FastAPI",
  "done": false
}
```

## Notes

Tasks are stored in memory, so they reset when the server restarts.

## Roadmap

- Update endpoint (mark a task as done)
- Database storage (SQLite, then PostgreSQL)
- Automated tests
- Docker support