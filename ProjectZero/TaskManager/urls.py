from django.urls import path
from . import views

name = 'TaskManager'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.task_list, name=''),
]