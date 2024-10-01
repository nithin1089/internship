# To-Do List Application

# Global list to store tasks
todo_list = []

# Function to display the current list of tasks
def display_tasks():
    if len(todo_list) == 0:
        print("\nYour To-Do list is empty.")
    else:
        print("\nYour To-Do list:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task():
    task = input("\nEnter the new task: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added.")

# Function to update a task
def update_task():
    display_tasks()
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[task_num - 1] = new_task
            print(f"Task {task_num} has been updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    display_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def complete_task():
    display_tasks()
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            task = todo_list[task_num - 1]
            todo_list[task_num - 1] = f"{task} (Completed)"
            print(f"Task {task_num} has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to show menu and handle user choices
def show_menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as completed")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            complete_task()
        elif choice == '6':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the To-Do List Application
show_menu()
