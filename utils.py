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