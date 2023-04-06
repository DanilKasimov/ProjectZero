from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models 
from django.views.decorators.csrf import csrf_exempt

def task_list(request):
    return render(request, 'TaskManager/index.html')

def test(request):
    return HttpResponse('OK')

@csrf_exempt
def create_task_type(request):
    task_type = models.TaskType(
        task_type_name = request.GET.get('name'), 
        task_type_code = request.GET.get('code')
    )
    task_type.save()
    return HttpResponse('OK')

@csrf_exempt
def get_task_types(request):
    return JsonResponse({'data' : [rec.to_dict() for rec in models.TaskType.objects.all()]})