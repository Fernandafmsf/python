from task import add_task, list_tasks, finish_task, remove_task


def main():
    tasks = []

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

if __name__ == "__main__":
    main()