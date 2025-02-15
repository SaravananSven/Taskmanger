from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.

def task_list(request):
    tasks=Task.objects.all()
    return render(request,'tasks/task_list.html',{'tasks':tasks})

def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form=TaskForm()
    return render(request,'tasks/add_task.html',{'form':form})

def edit_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def delete_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('task_list')
def filter_tasks(request,priority):
    tasks=Task.objects.filter(priority=priority)
    print(tasks)
    return render(request,'tasks/task_list.html',{'tasks':tasks})

def filterby_status(request, status):
    tasks = Task.objects.filter(status=status)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})