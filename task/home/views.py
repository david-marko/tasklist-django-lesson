from django.shortcuts import render, redirect

all_tasks = []

# Create your views here.
def homePage(request):
    for task in all_tasks:
        print(task['title'])
    context = {
        "all_tasks": all_tasks
    }
    return render(request, "index.html", context)


def addPage(request):
    error_message = None
    if request.method == 'POST':
        form_data = request.POST
        title = form_data['title']
        description = form_data['description']
        duedate = form_data['duedate']
        priority = form_data['priority']
        status = form_data['status']

        # count all items in alltasks and add 1
        task_count = len(all_tasks)
        new_id = task_count + 1

        task = {
            "id": new_id,
            "title": title,
            "description": description,
            "duedate": duedate,
            "priority": priority,
            "status" : status
        }

        # Check to see that the task does not exist
        isAlreadyCreated = title in [each['title'] for each in all_tasks]

        if isAlreadyCreated == False:
            all_tasks.append(task)
            return redirect('/')
        else:
            error_message = "The task '"+title+"' is already created."
            
    context = {
        "error": error_message
    }
    return render(request, "add.html", context)


def viewPage(request, task_id):
    demo_task = {}
    context = {
        "task": demo_task
    }
    return render(request, "view.html", context)