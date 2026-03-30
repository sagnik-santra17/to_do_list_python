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

            print(f"'{enter_username}' - User exists 🚻")
            utils.separator()

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
            print("Password can't be empty! ❌")

        elif enter_password == current_user["password"]:
            print("Login successful ✅")
            utils.separator()
            return current_user
        
        else:
            print("Wrong password ❌! Try again. 👈")

current_user = login_or_signup()

def add_task(current_user, existing_users, data): #Adding task function

    new_task_name = input("Enter task name: ").capitalize()  
    new_task_category = input("Enter task category: ").capitalize()  
    new_task_description = input("Enter task description: ").capitalize()  

    task = Task(new_task_name, new_task_category, new_task_description)

    current_user["tasks"].append(task.to_dict())
    print("Task added successfully ✅")
    utils.separator()
    data.save_data(existing_users)


def view_tasks(task_list, existing_users, data): #Viewing tasks function
    if not task_list:
        print("No tasks available")

    else:
        utils.display_tasks(task_list)

        while True:
            user_input = utils.valid_input_check("Choose a task id to mark it as completed: ", 1, len(task_list))
            print()

            task_list[user_input -1]["task_status"] = "Completed"
            print("Status updated 👍")
            utils.separator()
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
            print("Task deleted successfully! 👍")
            utils.separator()
            data.save_data(existing_users)
            break


def edit_task(task_list, existing_users, data): #Updating tasks
    if not task_list:
        print("No task to edit")
        print()

    else:
        print("Which task do you want to edit?")
        utils.separator()

        utils.display_tasks(task_list)

        while True:

            task_id = utils.valid_input_check("Enter task id: ", 1, len(task_list))

            current_task = task_list[task_id -1]

            while True:
                
                utils.separator()
                print("What do you want to edit?")
                print("1. Edit task name")
                print("2. Edit task category")
                print("3. Edit task status")
                print("4. Edit task description")
                print("5. Edit task creation date")
                print("6. Edit task due date")
                print("7. Edit task completion date")
                print("8. Main menu")
                utils.separator()

                edit_choice = utils.valid_input_check("Choose an action: ", 1, 8)

                if edit_choice == 1: #Edit task name

                    while True:
                        edited_task_name = input("Enter the modified task name: ").strip()

                        if not edited_task_name:
                            print("Please enter a valid modified task name 👈")
                        else:
                            old_task_name = current_task["task_name"]
                            current_task["task_name"] = edited_task_name

                            print()

                            print(f'"{old_task_name}" updated to "{edited_task_name}"')
                            print("Task name updated successfully! ✅")
                            utils.separator()
                            data.save_data(existing_users)
                            break   
                    
                
                elif edit_choice == 2: #Editing category

                    while True:
                        edited_category = input("Enter the new category: ").strip()

                        if not edited_category:
                            print("Please enter a valid category! 👈")

                        else:
                            old_category = current_task["task_category"]
                            current_task["task_category"] = edited_category

                            print()
                            
                            print(f'"{old_category}" updated to "{edited_category}"')
                            print("Category updated ✅")
                            utils.separator()
                            data.save_data(existing_users)
                            break

                elif edit_choice == 3: #Editing task status

                    while True:
                        edited_status = input("Enter the new status (Pending/Completed): ").lower().strip()

                        if not edited_status:
                            print("Please enter a valid status! 👈")

                        else:
                            if edited_status == "pending" or edited_status == "completed":
                                old_status = current_task["task_status"]
                                current_task["task_status"] = edited_status

                                print()

                                print(f'"{old_status}" updated to "{edited_status}"')
                                print("Status updated ✅")
                                utils.separator()
                                data.save_data(existing_users)
                                break

                            else:
                                print("Wrong input! ❌ Choose between 'Pending' or 'Completed' 👈")

                elif edit_choice == 4: #Editing description

                    while True:
                        edited_description = input("Enter the new description: ").strip()

                        if not edited_description:
                            print("Please enter a valid description! 👈")

                        else:
                            old_description = current_task["task_description"]
                            current_task["task_description"] = edited_description

                            print()

                            print(f'"{old_description}" updated to "{edited_description}"')
                            print("Description updated ✅")
                            utils.separator()
                            data.save_data(existing_users)
                            break

                elif edit_choice == 5: #Editing task creation date

                    while True:
                        edited_task_creation_date = input("Enter the new task creation date: ").strip()

                        if not edited_task_creation_date:
                            print("Please enter a valid task creation date! 👈")

                        else:
                            old_task_creattion_date = current_task["task_creation_date"]
                            current_task["task_creation_date"] = edited_task_creation_date

                            print()

                            print(f'"{old_task_creattion_date}" updated to "{edited_task_creation_date}"')
                            print("Task creation date updated ✅")
                            utils.separator()
                            data.save_data(existing_users)
                            break

                elif edit_choice == 6: #Editing due date
                    while True:
                        edited_due_date = input("Enter the new due date: ").strip()

                        if not edited_due_date:
                            print("Please enter a valid due date! 👈")

                        else:
                            old_due_date = current_task["task_due_date"]
                            current_task["task_due_date"] = edited_due_date

                            print()

                            print(f'"{old_due_date}" updated to "{edited_due_date}"')
                            print("Task due date updated ✅")
                            utils.separator()
                            data.save_data(existing_users)
                            break

                elif edit_choice == 7: #Editing task completion date
                    while True:
                        edited_completion_date = input("Enter the new completion date: ").strip()

                        if not edited_completion_date:
                            print("Please enter a valid completion date! 👈")

                        else:
                            old_completion_date = current_task["task_completion_date"]
                            current_task["task_completion_date"] = edited_completion_date

                            print()

                            print(f'"{old_completion_date}" updated to "{edited_completion_date}"')
                            print("Task completion date updated ✅")
                            utils.separator()
                            data.save_data(existing_users)
                            break

                elif edit_choice == 8: #Main menu
                    break

            break

def update_password(current_user, existing_users, data):
    while True:
        old_password = input("Enter your old password to proceed: ")

        if not old_password:
            print("Please enter a valid password 👈")
        elif old_password != current_user["password"]:
            print("Password didn't match! ❌ Please try again 👈")
            
        else:
            while True:
                new_password = input("Enter your new password: ")

                if not new_password:
                    print("Please enter a valid password 👈")
                elif new_password == current_user["password"]:
                    print("New password can't be the same as the old one! ❌")
                
                else:
                    current_user["password"] = new_password
                    print("Password updated successfully ✅")
                    utils.separator()
                    data.save_data(existing_users)
                    break
            break     


def search_task(current_user):

    def find_tasks():
        while True:
            task_keyword = input("Enter task keyword: ")
            utils.separator()
            found_tasks = []
            found = False

            for task in current_user["tasks"]:
                if task_keyword in task["task_name"]:
                    found_tasks.append(task)
                    found = True

                    print("Here are the tasks associated with your keyword:")
                    print()

                    utils.display_tasks(found_tasks)
                    return found_tasks

            if found == False:
                print("Keyword not found!")
                print()
                
                while True:
                    try:
                        print("Enter 1 to search agian")
                        print("Enter 2 to go to the main menu")
                        print()

                        action = int(input("Choose an action: "))

                        if 1 <= action <= 2:
                            if action == 1:
                                break

                            elif action == 2:
                                return []
                            
                    except ValueError:
                        print("Not a valid input! Please try again.")
    
    list_of_found_tasks = find_tasks()

    def edit_found_tasks(task_list):

        if task_list:
            print("Choose an action:")
            print("Enter 1 to edit tasks")
            print("Enter 2 to go to the main menu")

            while True:
                try:
                    print()
                    action = int(input("Choose action: "))
                    print()

                    if 1 <= action <= 2:
                        if action == 1:
                            edit_task(task_list, existing_users, data)
                            break
                        elif action == 2:
                            break

                except ValueError:
                    print("Wrong input! Please choose a valid option.")

        else:
            print("No task found!")

    edit_found_tasks(list_of_found_tasks)   







while True:
    print()
    print("===== MAIN MENU =====")
    print()
    print("1: View tasks")
    print("2: Add task")
    print("3: Delete task")
    print("4: Update task (edit, add dates, change status, etc...)")
    print("5: Update password")
    print("6: Search tasks")
    print("7: Exit")
    print()
    print("====================")
    print()

    user_input = utils.valid_input_check("Choose an action: ", 1, 7)
    print()

    if user_input == 2: #Add task
        add_task(current_user, existing_users, data)

    elif user_input == 1: #View tasks
        view_tasks(current_user["tasks"], existing_users, data)

    elif user_input == 3: #Delete task
        delete_task(current_user, existing_users, data)

    elif user_input == 4: #Update tasks
        edit_task(current_user["tasks"], existing_users, data)
    
    elif user_input == 5: #Update password
        update_password(current_user, existing_users, data)

    elif user_input == 6:
        search_task(current_user)

    elif user_input == 7: #Exit
        break



