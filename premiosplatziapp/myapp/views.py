from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    title = 'Django Course!!'
    return render(request, "index.html", {  
        'title': title
    })

def about(request):
    username = "asdru"
    return render(request, "about.html", {  
        'username': username
    })

def hello(request, user):
    return HttpResponse("<h2>Hello %s</h2>" % user)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects   
    })

def tasks(request):
    #task = Task.objects.get(title=title)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {  
        'tasks': tasks
    })

""" def iniciomyapp(request, id):
    result = (id + 100) * 2
    return HttpResponse("<h1> Hello %s</h1>" % result) """