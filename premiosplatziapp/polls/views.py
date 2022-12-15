from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse('<h1>About Polls...</h1>')
