import os
import json
import app

def test_add_and_load():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

    app.add_task("Test Task 1")
    tasks = app.load_tasks()
    assert tasks[0]["task"] == "Test Task 1"
    assert not tasks[0]["done"]
