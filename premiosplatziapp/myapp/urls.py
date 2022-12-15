from django.urls import path

from . import views

urlpatterns = [ 
    path('index/', views.index),
    path('hello/<str:user>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('About/', views.about),
]
    