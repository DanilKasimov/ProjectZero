from django.urls import path
from . import views

name = 'TaskManager'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.task_list, name=''),
    path('create_task_type', views.create_task_type, name='create_task_type'),
    path('get_task_types', views.get_task_types, name='get_task_types'),
]