from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
# Create your views here.


@login_required
def index(request):
    todo = Todo.objects.filter(user=request.user).order_by(
        '-created_at', 'is_complete')
    context = {'todo': todo}
    return render(request, 'index.html', context)


@login_required
def create(request):
    if request.method == "POST":
        todo_text = request.POST.get('todo')
        if todo_text:
            Todo.objects.create(todo=todo_text, user=request.user)
            return redirect('index')


@login_required
def update(request, pk):
    if request.POST.get('_method') == 'PUT':
        todo_text = request.POST.get('todo')
        if todo_text:
            todo = Todo.objects.get(id=pk, user=request.user)
            todo.todo = todo_text
            todo.save()
            return redirect('index')


@login_required
def delete(request, pk):
    if request.POST.get('_method') == 'DELETE':
        todo = Todo.objects.get(id=pk, user=request.user)
        if todo:
            todo.delete()
            return redirect('index')


@login_required
def complete(request, pk):
    if request.POST.get('_method') == 'PUT':
        todo = Todo.objects.get(id=pk, user=request.user)
        if todo:
            todo.is_complete = False if todo.is_complete else True
            todo.save()
            return redirect('index')
