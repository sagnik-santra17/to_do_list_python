from task import Task

def main_task_func(task_item): #Prints the task details

    task_obj = Task(task_item["task_name"],
                    task_item["task_category"],
                    task_item["task_description"],
                )
    task_obj.task_status = task_item["task_status"]
    task_obj.task_creation_date = task_item["task_creation_date"]
    task_obj.task_due_date = task_item["task_due_date"]
    task_obj.task_completion_date = task_item["task_completion_date"]

    return task_obj


def display_tasks(task_list): #Display task list inside the main script

    for task_number, task_item in enumerate(task_list, start=1):
        task_obj = main_task_func(task_item)
        status = task_obj.task_status.lower()

        creation_date = task_obj.task_creation_date
        due_date = task_obj.task_due_date
        completion_date = task_obj.task_completion_date

        creation_date = creation_date if creation_date else "DD/MM/YY"
        due_date = due_date if due_date else "DD/MM/YY"
        completion_date = completion_date if completion_date else "DD/MM/YY"


        if status == "completed":
             status_symbol = "✅"
        else:
            status_symbol = "[  ]"

        print(f"[{task_number}] {task_obj.task_name}")
        print()
        print(f"    Category: {task_obj.task_category}")
        print(f"    Description: {task_obj.task_description}")
        print(f"    Status: {task_obj.task_status} {status_symbol}")
        print(f"    Creation date: {creation_date}")
        print(f"    Due date: {due_date}")
        print(f"    Completion date: {completion_date}")
        separator()


def valid_input_check(prompt, min, max): #Input validation check
    
    while True:
        try:
            num = int(input(prompt))

            if min <= num <= max:
                return num
            else:
                print("Please enter a number bewtween 1 and 6")
        
        except ValueError:
            print("Invalid input! Enter a valid input.")


def separator():
    print()
    print("--------------------------------")
    print()









