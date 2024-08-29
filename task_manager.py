import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the text file."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task_descriptions):
    """Add new tasks to the list with a [Pending] status."""
    tasks = load_tasks()
    new_tasks = task_descriptions.split(',')
    existing_tasks = [task[10:].strip() for task in tasks if task.startswith("[Pending]")]
    
    for description in new_tasks:
        description = description.strip()
        if description in existing_tasks:
            print(f"Task '{description}' already exists. You can't add duplicate pending tasks.")
        else:
            task = f"[Pending] {description}"
            tasks.append(task)
            print(f"Task added: {description}")
    
    save_tasks(tasks)

def list_tasks():
    """View all tasks with their status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def complete_task(task_numbers):
    """Mark tasks as completed."""
    tasks = load_tasks()
    task_numbers = [int(num.strip()) for num in task_numbers.split(',')]
    
    for number in task_numbers:
        if 1 <= number <= len(tasks):
            task = tasks[number - 1]
            if task.startswith("[Pending]"):
                tasks[number - 1] = task.replace("[Pending]", "[Completed]")
                print(f"Task completed: {task[10:].strip()}")
            else:
                print(f"Task {number} is already completed.")
        else:
            print(f"Invalid task number: {number}")
    
    save_tasks(tasks)

def delete_task(task_numbers):
    """Delete tasks from the list."""
    tasks = load_tasks()
    task_numbers = sorted([int(num.strip()) for num in task_numbers.split(',')], reverse=True)
    
    for number in task_numbers:
        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print(f"Task deleted: {deleted_task[10:].strip()}")
        else:
            print(f"Invalid task number: {number}")
    
    save_tasks(tasks)

def main():
    """Main function to handle user choice."""
    while True:
        print("\nTask Manager CLI")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Complete Tasks")
        print("4. Delete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task_descriptions = input("Enter the task descriptions separated by commas: ")
            add_task(task_descriptions)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_numbers = input("Enter the task numbers to complete separated by commas: ")
            complete_task(task_numbers)
        elif choice == '4':
            task_numbers = input("Enter the task numbers to delete separated by commas: ")
            delete_task(task_numbers)
        elif choice == '5':
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
