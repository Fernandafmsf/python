name = input("What is your name? ") 

tasks = []

def add_task():
    title = input("Whats the task title?")
    status = input("Whats the task status?")
    tasks.append({
        "title": title,
        "status": status
    })

def list_tasks(tasks):
    for task in tasks:
        print(f"Title: {task['title']}, Status: {task['status']}")

def finish_task(task):
    list_tasks(tasks)
    task_title = input("Enter the title of the task to finish: ")
    for task in tasks: 
            if task["title"] == task_title:
                task["status"] = "completed"
                print(f"Task '{task_title}' marked as completed.")
                break
    else:
        print(f"Task '{task_title}' not found.")

def remove_task(task):
    list_tasks(tasks)
    task_title = input("Enter the title of the task to remove: ")
    for task in tasks:
        if task['title'] == task_title:
            tasks.remove(task)
            print(f"Task '{task_title}' removed.")
            break
    else:
        print(f"Task '{task_title}' not found.")

while True:
    print("\n --- Menu ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Finish task")
    print("4. Remove task")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_task()
    elif option == "2":
        list_tasks(tasks)
    elif option == "3":
        finish_task(tasks)
    elif option == "4":
        remove_task(tasks)
    elif option == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")