from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):
    valid, msg = validate_task_title(title)
    if not valid:
        print(msg)
        return False

    valid, msg = validate_task_description(description)
    if not valid:
        print(msg)
        return False

    valid, msg = validate_due_date(due_date)
    if not valid:
        print(msg)
        return False

    tasks.append({
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")
    return True


def mark_task_as_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
        return True

    print("Invalid task index.")
    return False


def view_pending_tasks(tasks):
    return [task for task in tasks if not task["completed"]]


def calculate_progress(tasks):
    if not tasks:
        return 0

    completed = sum(task["completed"] for task in tasks)
    return (completed / len(tasks)) * 100