from django.db import models

class TaskType(models.Model):
    task_type_id = models.AutoField('Идентификатор типа задачи', primary_key=True)
    task_type_name = models.CharField('Наименование типа задачи', max_length=512)
    task_type_code = models.CharField('Код типа задачи', max_length=10)

class Task(models.Model):
    task_id = models.AutoField('Идентификатор задачи', primary_key=True)
    task_type_id = models.ForeignKey(TaskType, on_delete=models.PROTECT)