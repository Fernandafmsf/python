name = input("What is your name? ") 

tasks = []

def add_task(title, status):
    tasks.append({
        "title": title,
        "status": status
    })

def list_tasks(tasks):
    for task in tasks:
        print(f"Title: {task['title']}, Status: {task['status']}")

def finish_task(task):
    task["status"] = "completed"

def remove_task(task):
    tasks.remove(task)

while True:
    print("\n --- Menu ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Finish task")
    print("4. Remove task")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        title  = input("Whats the task title?")
        status = input("Whats the task status?")

        add_task(title, status)
    elif option == "2":
        list_tasks(tasks)
    elif option == "3":
        list_tasks(tasks)
        task_title = input("Enter the title of the task to finish: ")
        for task in tasks:
            if task["title"] == task_title:
                finish_task(task)
                print(f"Task '{task_title}' marked as completed.")
                break
        else:
            print(f"Task '{task_title}' not found.")    
    elif option == "4":
        list_tasks(tasks)
        task_title = input("Enter the title of the task to remove: ")
        for task in tasks:
            if task["title"] == task_title:
                remove_task(task)
                print(f"Task '{task_title}' removed.")
                break
        else:
            print(f"Task '{task_title}' not found.")    
    elif option == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")