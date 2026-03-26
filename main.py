from data_manager import DataManager
from task import Task
import utils

#Main menu
print()
print("~*~*~* Welcome to out to-do-list ~*~*~*")
print()

data = DataManager()

existing_users = data.load_data()

enter_username = input("Enter your username: ")

user_found = False
current_user = None

for entry in existing_users["users"]:
    if entry["username"] == enter_username:
        print()
        print(f"'{enter_username}' - User exists")
        user_found = True

        current_user = entry
        break
    
if not user_found:
    existing_users["users"].append({
    "username": enter_username,
    "tasks": []
    })
    current_user = existing_users["users"][-1]

while True:
    print()
    print("1: View tasks")
    print("2: Add task")
    print("3: Delete task")
    print("4: Update task")
    print("10: Exit")
    print()

    try:
        user_input = int(input("Choose an action: "))
        print()

        if 1 <= user_input <= 11:

            if user_input == 2: #Add task

                if current_user:
                    new_task_name = input("Enter task name: ")  
                    new_task_category = input("Enter task category: ")
                    new_task_description = input("Enter task description: ")

                    task = Task(new_task_name, new_task_category, new_task_description)

                    current_user["tasks"].append(task.to_dict())
                    data.save_data(existing_users)

            elif user_input == 1: #View tasks
                if not current_user["tasks"]:
                    print("No tasks available")
                else:
                    for task_number, task_item in enumerate(current_user["tasks"], start=1):
                        print(f"Task Id: {task_number}")    
                        print(f"{utils.main_task_func(task_item)}\n")

                    while True:
                        try:
                            choose_task_number = int(input("Choose a task Id: "))
                            print()

                            if 1 <= choose_task_number <= len(current_user["tasks"]):
                                current_user["tasks"][choose_task_number -1]["task_status"] = "Completed"
                                print("Status updated")
                                data.save_data(existing_users)
                                break

                            else:
                                print("Wrong input")

                        except ValueError:
                            print("Wrong input! Please pick again.")
            
            elif user_input == 3: #Delete task
                if not current_user["tasks"]:
                    print("No task to delete")
                    print()

                else:
                    while True:
                        for task_number, task_item in enumerate(current_user["tasks"], start=1):
                            print(f"Task Id: {task_number}")    
                            print(f"{utils.main_task_func(task_item)}\n")
                    
                        try:
                            delete_task_id = int(input("Choose a task id to delete: "))
                            print()

                            if 1 <= delete_task_id <= len(current_user["tasks"]):
                                del(current_user["tasks"][delete_task_id -1])
                                print("Task deleted succesfully!")
                                data.save_data(existing_users)
                                break
                            else:
                                print("Wrong input")

                        except ValueError:
                            print("Please pick a valid Id: ")

            elif user_input == 4: #Edit tasks
                if not current_user["tasks"]:
                    print("No task to edit")
                    print()

                else:
                    print("Which task do you want to edit?")
                    print()
                    for task_number, task_item in enumerate(current_user["tasks"], start=1):
                            print(f"Task Id: {task_number}")    
                            print(f"{utils.main_task_func(task_item)}\n")

                    while True:

                        try:
                            edit_task_id = int(input("Enter task id: "))
    
                            if  1 <= edit_task_id <= len(current_user["tasks"]):
                                print()
                                print("What do you want to edit?")
                                print("1. Edit task name")
                                print("2. Edit task category")
                                print("3. Edit task description")
                                print("4. Edit task creation date")
                                print("5. Edit task due date")
                                print("6. Edit task completion date")
                                print()


                                try:
                                    edit_action_num = int(input("Choose an action: "))

                                    if 1 <= edit_action_num <= 6:
                                        if edit_action_num == 1:
                                            edited_task_name = input("Enter the modified task name: ")

                                            current_user["tasks"][edit_task_id -1]["task_name"] = edited_task_name
                                            print("Task name upadated successfully!")
                                            data.save_data(existing_users)
                                            break
                                        
                                        

                                    else:
                                        print("Please pick a valid action!")




                                except ValueError:
                                    print("Invalid input! Please enter a valid input.")
                
                        except ValueError:
                            print("Invalid input! Please enter a valid input.")

            elif user_input == 10: #Exit
                break

        else:
            print("Wrong input")
    
    except ValueError:
        print("Wrong input! Please enter a number")