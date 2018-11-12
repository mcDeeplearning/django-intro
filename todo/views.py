from django.shortcuts import render
from todo.models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request,'todo/index.html',{'todos':todos})
    
def new(request):
    # 사용자가 입력할 수 있는 폼을 만들어 주기
    return render(request,'todo/new.html')
