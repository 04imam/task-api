\# Task API



A simple REST API built with Python and FastAPI. This is a learning project from my backend roadmap.



\## Endpoints



\- `GET /` : returns a hello message

\- `GET /tasks` : returns all tasks

\- `GET /tasks/{id}` : returns one task by its ID

\- `POST /tasks` : adds a new task

\- `DELETE /tasks/{id}` : deletes a task



\## How to run



```

python -m venv .venv

.venv\\Scripts\\Activate.ps1

pip install fastapi "uvicorn\[standard]"

uvicorn main:app --reload

```



Then open http://127.0.0.1:8000/docs to test the endpoints.



\## Note



Tasks are stored in memory, so they reset when the server restarts. A real database is planned as a next step.

