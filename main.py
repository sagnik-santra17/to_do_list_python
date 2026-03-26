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

        print(f"'{enter_username}' - User exists")
        user_found = True

        current_user = entry
        print()
        enter_password = input("Enter your password: ")
        break
    
if not user_found:
    enter_password = input("Generate your password: ")
    existing_users["users"].append({
    "username": enter_username,
    "password": enter_password,
    "tasks": []
    })
    current_user = existing_users["users"][-1]
    data.save_data(existing_users)

while True:
    
    if not enter_password:
        print("Password can't be empty!")
        enter_password = input("Enter your password: ")

    elif enter_password == current_user["password"]:

        while True:
            print()
            print("1: View tasks")
            print("2: Add task")
            print("3: Delete task")
            print("4: Update task (edit, add dates, change status, etc...)")
            print("5: Update password")
            print("6: Exit")
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
                                    choose_task_number = int(input("Choose a task id to mark it as completed: "))
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
                                        current_task = current_user["tasks"][edit_task_id -1]

                                        while True:
                                            try:
                                                print()
                                                print("What do you want to edit?")
                                                print("1. Edit task name")
                                                print("2. Edit task category")
                                                print("3. Edit task status")
                                                print("4. Edit task description")
                                                print("5. Edit task creation date")
                                                print("6. Edit task due date")
                                                print("7. Edit task completion date")
                                                print("8. Main menu")
                                                print()

                                                edit_action_num = int(input("Choose an action: "))

                                                if 1 <= edit_action_num <= 8:

                                                    if edit_action_num == 1: #Edit task name

                                                        while True:
                                                            edited_task_name = input("Enter the modified task name: ").strip()

                                                            if not edited_task_name:
                                                                print("Please enter a valid modified task name")
                                                            else:
                                                                old_task_name = current_task["task_name"]
                                                                current_task["task_name"] = edited_task_name

                                                                print()

                                                                print(f'"{old_task_name}" updated to "{edited_task_name}"')
                                                                print("Task name updated successfully!")
                                                                data.save_data(existing_users)
                                                                break   
                                                        
                                                    
                                                    elif edit_action_num == 2: #Editing category

                                                        while True:
                                                            edited_category = input("Enter the new category: ").strip()

                                                            if not edited_category:
                                                                print("Please enter a valid category!")

                                                            else:
                                                                old_category = current_task["task_category"]
                                                                current_task["task_category"] = edited_category

                                                                print()
                                                                
                                                                print(f'"{old_category}" updated to "{edited_category}"')
                                                                print("Category updated")
                                                                data.save_data(existing_users)
                                                                break

                                                    elif edit_action_num == 3: #Editing task status

                                                        while True:
                                                            edited_status = input("Enter the new status: ").strip()

                                                            if not edited_status:
                                                                print("Please enter a valid status!")

                                                            else:
                                                                old_status = current_task["task_status"]
                                                                current_task["task_status"] = edited_status

                                                                print()

                                                                print(f'"{old_status}" updated to "{edited_status}"')
                                                                print("Status updated")
                                                                data.save_data(existing_users)
                                                                break

                                                    elif edit_action_num == 4: #Editing description

                                                        while True:
                                                            edited_description = input("Enter the new description: ").strip()

                                                            if not edited_description:
                                                                print("Please enter a valid description!")

                                                            else:
                                                                old_description = current_task["task_description"]
                                                                current_task["task_description"] = edited_description

                                                                print()

                                                                print(f'"{old_description}" updated to "{edited_description}"')
                                                                print("Description updated")
                                                                data.save_data(existing_users)
                                                                break

                                                    elif edit_action_num == 5: #Editing task creation date

                                                        while True:
                                                            edited_task_creation_date = input("Enter the new task creation date: ").strip()

                                                            if not edited_task_creation_date:
                                                                print("Please enter a valid task creation date!")

                                                            else:
                                                                old_task_creattion_date = current_task["task_creation_date"]
                                                                current_task["task_creation_date"] = edited_task_creation_date

                                                                print()

                                                                print(f'"{old_task_creattion_date}" updated to "{edited_task_creation_date}"')
                                                                print("Task creation date updated")
                                                                data.save_data(existing_users)
                                                                break

                                                    elif edit_action_num == 6: #Editing due date
                                                        while True:
                                                            edited_due_date = input("Enter the new due date: ").strip()

                                                            if not edited_due_date:
                                                                print("Please enter a valid due date!")

                                                            else:
                                                                old_due_date = current_task["task_due_date"]
                                                                current_task["task_due_date"] = edited_due_date

                                                                print()

                                                                print(f'"{old_due_date}" updated to "{edited_due_date}"')
                                                                print("Task due date updated")
                                                                data.save_data(existing_users)
                                                                break

                                                    elif edit_action_num == 7: #Editing task completion date
                                                        while True:
                                                            edited_completion_date = input("Enter the new completion date: ").strip()

                                                            if not edited_completion_date:
                                                                print("Please enter a valid completion date!")

                                                            else:
                                                                old_completion_date = current_task["task_completion_date"]
                                                                current_task["task_completion_date"] = edited_completion_date

                                                                print()

                                                                print(f'"{old_completion_date}" updated to "{edited_completion_date}"')
                                                                print("Task completion date updated")
                                                                data.save_data(existing_users)
                                                                break



                                                    elif edit_action_num == 8: #Main menu
                                                        break

                                                else:
                                                    print("Please pick a valid action!")

                                            except ValueError:
                                                print("Invalid input! Please enter a valid input.")
                                    break
                        
                                except ValueError:
                                    print("Invalid input! Please enter a valid input.")

                    elif user_input == 6: #Exit
                        break

                else:
                    print("Wrong input")
            
            except ValueError:
                print("Wrong input! Please enter a number")

        break

    else:
        print("Wrong password! Try again.")
        enter_password = input("Enter your password: ")