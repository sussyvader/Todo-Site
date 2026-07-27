from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,render
from .models import Todo

# Create your views here.
def addTask(request):
    tas=request.POST['task']
    print(tas)
    Todo.objects.create(task=tas)
    return redirect('home')

def mad(request,pk):
    task=get_object_or_404(Todo, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mau(request,pk):
    task=get_object_or_404(Todo, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def dele(request,pk):
    task=get_object_or_404(Todo, pk=pk)
    task.delete()
    return redirect('home')

def edit(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    if request.method == "POST":
        task.task = request.POST.get('task')
        task.save()
        return redirect('home')
    else:
        return redirect(f"/?edit={pk}")
