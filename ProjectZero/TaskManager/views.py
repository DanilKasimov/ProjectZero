from django.shortcuts import render
from django.http import HttpResponse

def task_list(request):
    return render(request, 'TaskManager/index.html')

def test(request):
    return HttpResponse('OK')