from django.shortcuts import render, redirect, get_object_or_404
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


def update(request, pk):
    if request.POST.get('_method') == 'PUT':
        todo_text = request.POST.get('todo')
        if todo_text:
            todo = Todo.objects.get(id=pk)
            todo.todo = todo_text
            todo.save()
            return redirect('index')


def delete(request, pk):
    if request.POST.get('_method') == 'DELETE':
        todo = Todo.objects.get(id=pk)
        if todo:
            todo.delete()
            return redirect('index')
