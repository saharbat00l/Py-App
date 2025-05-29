import os
import json
import cli_app  # Instead of 'app'

def test_add_and_load():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

    cli_app.add_task("Test Task 1")
    tasks = cli_app.load_tasks()
    assert tasks[0]["task"] == "Test Task 1"
    assert not tasks[0]["done"]
