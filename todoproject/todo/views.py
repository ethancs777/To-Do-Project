from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def task_management(request):
    return render(request, 'todo/task_management.html')

def view_tasks(request):
    return render(request, 'todo/view_tasks.html')