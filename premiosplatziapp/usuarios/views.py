from django.shortcuts import render

# Create your views here.

def inicioUsuarios(request):
    return render(request, "inicioUsuarios.html")