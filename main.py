from data_manager import DataManager
from task import Task
import utils

#Main menu
print()
print("~*~*~* Welcome to out to-do-list ~*~*~*")
print()

data = DataManager()
existing_users = data.load_data()

def login_or_signup():

    enter_username = input("Enter your username: ")
    user_found = False
    current_user = None
    
    for entry in existing_users["users"]:
        if entry["username"] == enter_username:

            print(f"'{enter_username}' - User exists")
            user_found = True

            current_user = entry
            print()
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

        return current_user

    while True:
        enter_password = input("Enter your password: ")
        
        if not enter_password:
            print("Password can't be empty!")

        elif enter_password == current_user["password"]:
            print("Login successful")
            return current_user
        
        else:
            print("Wrong password! Try again.")

current_user = login_or_signup()

def add_task(current_user, existing_users, data): #Adding task function

    new_task_name = input("Enter task name: ")  
    new_task_category = input("Enter task category: ")
    new_task_description = input("Enter task description: ")

    task = Task(new_task_name, new_task_category, new_task_description)

    current_user["tasks"].append(task.to_dict())
    data.save_data(existing_users)

 
def view_tasks(current_user, existing_users, data): #Viewing tasks function
    if not current_user["tasks"]:
        print("No tasks available")

    else:
        utils.display_tasks(current_user["tasks"])

        while True:
            user_input = utils.valid_input_check("Choose a task id to mark it as completed: ", 1, len(current_user["tasks"]))
            print()

            current_user["tasks"][user_input -1]["task_status"] = "Completed"
            print("Status updated")
            data.save_data(existing_users)
            break


def delete_task(current_user, existing_users, data): #Deleting tasks funciton
    if not current_user["tasks"]:
        print("No task to delete")
        print()

    else:
        while True:
            utils.display_tasks(current_user["tasks"])
        
            user_input = utils.valid_input_check("Choose a task id to delete: ", 1, len(current_user["tasks"]))
            print()

            del(current_user["tasks"][user_input -1])
            print("Task deleted successfully!")
            data.save_data(existing_users)
            break

def edit_task(current_user, existing_users, data): #Editing tasks
    if not current_user["tasks"]:
        print("No task to edit")
        print()

    else:
        print("Which task do you want to edit?")
        print()

        utils.display_tasks(current_user["tasks"])

        while True:

            task_id = utils.valid_input_check("Enter task id: ", 1, len(current_user["tasks"]))

            current_task = current_user["tasks"][task_id -1]

            while True:

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

                edit_choice = utils.valid_input_check("Choose an action: ", 1, 8)

                if edit_choice == 1: #Edit task name

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
                    
                
                elif edit_choice == 2: #Editing category

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

                elif edit_choice == 3: #Editing task status

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

                elif edit_choice == 4: #Editing description

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

                elif edit_choice == 5: #Editing task creation date

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

                elif edit_choice == 6: #Editing due date
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

                elif edit_choice == 7: #Editing task completion date
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

                elif edit_choice == 8: #Main menu
                    break

            break


while True:
    print()
    print("1: View tasks")
    print("2: Add task")
    print("3: Delete task")
    print("4: Update task (edit, add dates, change status, etc...)")
    print("5: Update password")
    print("6: Exit")
    print()

    user_input = utils.valid_input_check("Choose an action: ", 1, 6)
    print()

    if user_input == 2: #Add task
        add_task(current_user, existing_users, data)

    elif user_input == 1: #View tasks
        view_tasks(current_user, existing_users, data)

    elif user_input == 3: #Delete task
        delete_task(current_user, existing_users, data)

    elif user_input == 4: #Edit tasks
        edit_task(current_user, existing_users, data)

    elif user_input == 6: #Exit
        break



