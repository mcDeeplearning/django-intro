from django.shortcuts import render,redirect
from todo.models import Todo

# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request,'todo/index.html',{'todos':todos})
    
def new(request):
    # 사용자가 입력할 수 있는 폼을 만들어 주기
    return render(request,'todo/new.html')

# @csrf_exempt
def create(request):
    title = request.POST.get('title')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title,deadline=deadline)
    todo.save()
     
    return redirect('/todos/')

def read(request,id):
    todo = Todo.objects.get(id=id)
    return render(request,'todo/read.html',{'todo':todo})
    
def todo_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        # todo = Todo(title=title,deadline=deadlin)
        # todo.save()
        Todo.objects.create(title=title,deadline=deadline)
        return redirect('/todos/')
    else:
        return render(request,'todo/todo_create.html')
        
    
    
    