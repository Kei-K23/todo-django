from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def index(request):
    todo = Todo.objects.order_by('-updated_at')
    context = {'todo': todo}
    return render(request, 'index.html', context)


def create(request):
    if request.method == "POST":
        todo_text = request.POST.get('todo')
        if todo_text:
            Todo.objects.create(todo=todo_text)
            return redirect('index')
