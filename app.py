from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks = load_tasks()
    tasks.append({"task": data.get("task", ""), "done": False})
    save_tasks(tasks)
    return jsonify({"message": "Task added."}), 201

@app.route('/tasks/<int:index>/done', methods=['POST'])
def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        return jsonify({"message": f"Task {index + 1} marked as done."})
    return jsonify({"error": "Invalid task index"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
