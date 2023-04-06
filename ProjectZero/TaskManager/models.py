from django.db import models

class TaskType(models.Model):
    task_type_id = models.AutoField('Идентификатор типа задачи', primary_key=True)
    task_type_name = models.CharField('Наименование типа задачи', max_length=512)
    task_type_code = models.CharField('Код типа задачи', max_length=10)

class TaskState(models.Model):
    task_state_id = models.AutoField('Идентификатор состояния задачи', primary_key=True)
    task_state_name = models.CharField('Наименование состояния задачи', max_length=512)
    task_state_code = models.CharField('Код состояния задачи', max_length=10)

class Person(models.Model):
    person_id = models.AutoField('Идентификатор пользователя', primary_key=True)
    person_last_name = models.CharField('Фамилия', max_length=512)
    person_firs_name = models.CharField('Имя', max_length=512)
    person_sec_name = models.CharField('Отчество', max_length=512)
    person_login = models.CharField('Логин', max_length=512)
    person_password = models.CharField('Пароль', max_length=512)
    person_is_active = models.BooleanField('Is active', default=True)

class Task(models.Model):
    task_id = models.AutoField('Идентификатор задачи', primary_key=True)
    task_type_id = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    task_state_id = models.ForeignKey(TaskState, on_delete=models.PROTECT)
    task_title = models.CharField('Заголовок задачи', max_length=512)
    task_text = models.TextField('Текст задачи')
    task_created_time = models.DateTimeField('Дата создания задачи', auto_now_add=True)
    task_executer = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, related_name='executer')
    task_autor = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, related_name='author')

class Comment(models.Model):
    comment_id = models.AutoField('Идентификатор комментария', primary_key=True)
    comment_autor = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    comment_task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment_text = models.TextField('Текст комментария')
    comment_time = models.DateTimeField('Дата создания комментария', auto_now_add=True)

class Tag(models.Model):
    tag_id = models.AutoField('Идентификатор тэга', primary_key=True)
    tag_name = models.CharField('Название тэга', max_length=512)
    tag_code = models.CharField('Код тэга', max_length=512)

class TaskTags(models.Model):
    link_id = models.AutoField('Идентификатор связи', primary_key=True)
    link_task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    link_tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

