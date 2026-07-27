from django.shortcuts import render
from Todo.models import Todo

def home(request):
    tasks= Todo.objects.filter(is_completed=False)
    un_tasks= Todo.objects.filter(is_completed=True)
    edit_id = request.GET.get('edit')
    context = {
        'tasks' : tasks,
        'un' : un_tasks,
        'edit_id' : int(edit_id) if edit_id else None,
    }
    return render(request,'home.html', context)