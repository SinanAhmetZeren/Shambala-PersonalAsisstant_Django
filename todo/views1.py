from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import todo
from .forms import todoform
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#def todos(request):
#    todos = todo.objects.all()
#    return render(request,"todos.html",{"todos":todos})

def addtodo(request):
    pass

@login_required(login_url = "user:login")
def todos(request):
    form = todoform(request.POST or None)
    if form.is_valid():
        new_todo = form.save(commit=False)
        new_todo.author = request.user
        new_todo.save()
        #messages.success(request,"todo added")
        #return redirect("todos.html",
    todo_list = todo.objects.filter(author = request.user)
    return render(request,"todos.html",{"todo_list":todo_list})
    #return render(request,"addtodo.html",{"form":form})



@login_required(login_url = "user:login")
def updatetodo(request,id):
    new_todo = get_object_or_404(todo,id = id)
    form = todoform(request.POST or None,instance = new_todo)
    if form.is_valid():
        new_todo = form.save(commit=False)     
        new_todo.author = request.user
        new_todo.save()
        messages.success(request,"Todo updated")
        return redirect("/todos")
    return render(request,"updatetodo.html",{"form":form})



@login_required(login_url = "user:login")
def deletetodo(request,id):
    todo1 = get_object_or_404(todo,id = id)
    todo1.delete()
    messages.success(request,"Todo deleted")
    return redirect("/todos")
