from fastapi import FastAPI, Request

app = FastAPI()

tasks={}


@app.post("/api/tasks")
async def add_task(request: Request):
    task_data = await request.json()
    task_name = task_data.get("name")
    description = task_data.get("description")

    task_id = len(tasks) + 1
    tasks[task_id] = {
        "id": task_id,
        "name": task_name,
        "description": description,
        "completed": False
    }
    if task_name is None :
        return {"error": "Task name is required"}
    return {"message": "Task added", "data": tasks[task_id]}

@app.get("/api/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.put("/api/tasks/{id}")
async def update_task(id: int, request: Request):
    if id not in tasks:
        return {"error": "Task not found"}

    task_data = await request.json()
    name = task_data.get("name")
    description = task_data.get("description")
    completed = task_data.get("completed")
    if name is not None:
        tasks[id]["name"] = name
    if description is not None:
        tasks[id]["description"] = description
    if completed is not None:
        tasks[id]["completed"] = completed

    return {"message": "Task updated", "data": tasks[id]}




@app.get("/api/tasks/{id}")
def get_task(id: int):
    return tasks.get(id, {"error": "Task not found"})


@app.delete("/api/tasks/{id}")
def delete_task(id: int):
    if id in tasks:
        del tasks[id]
        return {"message": "Task deleted"}
    return {"error": "Task not found"}


