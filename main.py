tasks = []


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f.readlines():
                tasks.append(line.strip())
    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task():
    task = input("Enter task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append(task)
    save_tasks()

    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        num = int(input("\nEnter task number to delete: "))

        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"Deleted task: {removed}")

        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


load_tasks()

while True:
    print("\n====== TODO APP ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

        