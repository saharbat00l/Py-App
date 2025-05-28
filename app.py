import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Added task: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. [{status}] {t['task']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked task {index + 1} as done.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
