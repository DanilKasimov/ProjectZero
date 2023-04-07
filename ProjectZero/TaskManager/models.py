from django.db import models

class TaskType(models.Model):
    task_type_id = models.AutoField('Идентификатор типа задачи', primary_key=True)
    task_type_name = models.CharField('Наименование типа задачи', max_length=512)
    task_type_code = models.CharField('Код типа задачи', max_length=10)

    def __str__(self):
        return f'''
            TaskType:
                task_type_id: {self.task_type_id}, 
                task_type_name: {self.task_type_name}, 
                task_type_code: {self.task_type_code}
        '''
    
    def to_dict(self):
        return {
            'task_type_id' : self.task_type_id,
            'task_type_name' : self.task_type_name,
            'task_type_code' : self.task_type_code
        }

class TaskState(models.Model):
    task_state_id = models.AutoField('Идентификатор состояния задачи', primary_key=True)
    task_state_name = models.CharField('Наименование состояния задачи', max_length=512)
    task_state_code = models.CharField('Код состояния задачи', max_length=10)
    
    def __str__(self):
        return f''''
            TaskState:
                task_state_id: {self.task_state_id}, 
                task_state_name: {self.task_state_name}, 
                task_state_code: {self.task_state_code}
        '''
    
    def to_dict(self):
        return {
            'task_state_id' : self.task_state_id,
            'task_state_name' : self.task_state_name,
            'task_state_code' : self.task_state_code
        }
    
class Person(models.Model):
    person_id = models.AutoField('Идентификатор пользователя', primary_key=True)
    person_last_name = models.CharField('Фамилия', max_length=512)
    person_firs_name = models.CharField('Имя', max_length=512)
    person_sec_name = models.CharField('Отчество', max_length=512)
    person_login = models.CharField('Логин', max_length=512)
    person_password = models.CharField('Пароль', max_length=512)
    person_is_active = models.BooleanField('Is active', default=True)

    def __str__(self):
        return f'''
            Person:
                person_id: {self.person_id}, 
                person_last_name: {self.person_last_name}, 
                person_firs_name: {self.person_firs_name}, 
                person_sec_name: {self.person_sec_name}, 
                person_login: {self.person_login}, 
                person_password: {self.person_password}, 
                person_is_active: {self.person_is_active}
        '''
    
    def to_dict(self):
        return {
            'person_id' : self.person_id,
            'person_last_name' : self.person_last_name,
            'person_firs_name' : self.person_firs_name,
            'person_sec_name' : self.person_sec_name,
            'person_login' : self.person_login,
            'person_password' : self.person_password,
            'person_is_active' : self.person_is_active
        }

class Task(models.Model):
    task_id = models.AutoField('Идентификатор задачи', primary_key=True)
    task_type_id = models.ForeignKey(TaskType, on_delete=models.PROTECT, related_name='fk_task_type')
    task_state_id = models.ForeignKey(TaskState, on_delete=models.PROTECT, related_name='fk_task_state')
    task_title = models.CharField('Заголовок задачи', max_length=512)
    task_text = models.TextField('Текст задачи')
    task_created_time = models.DateTimeField('Дата создания задачи', auto_now_add=True)
    task_executor = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, related_name='fk_task_executor')
    task_autor = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, related_name='fk_task_author')

    def __str__(self):
        return f'''
            Task:
                task_id: {self.task_id},
                task_type_id: {self.task_type_id},
                task_state_id: {self.task_state_id},
                task_title: {self.task_title},
                task_text: {self.task_text},
                task_created_time: {self.task_created_time},
                task_executor: {self.task_executor},
                task_autor: {self.task_autor}
        '''
    
    def to_dict(self):
        return {
            'task_id' : self.task_id,
            'task_type_id' : self.task_type_id,
            'task_state_id' : self.task_state_id,
            'task_title' : self.task_title,
            'task_text' : self.task_text,
            'task_created_time' : self.task_created_time,
            'task_executor' : self.task_executor,
            'task_autor' : self.task_autor
        }

class Comment(models.Model):
    comment_id = models.AutoField('Идентификатор комментария', primary_key=True)
    comment_autor = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, related_name='fk_comment_author')
    comment_task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='fk_comment_task')
    comment_text = models.TextField('Текст комментария')
    comment_time = models.DateTimeField('Дата создания комментария', auto_now_add=True)

    def __str__(self):
        return f'''
            Comment:
                comment_id: {self.comment_id},
                comment_autor: {self.comment_autor},
                comment_task_id: {self.comment_task_id},
                comment_text: {self.comment_text},
                comment_time: {self.comment_time}
        '''
    
    def to_dict(self):
        return {
            'comment_id' : self.comment_id,
            'comment_autor' : self.comment_autor,
            'comment_task_id' : self.comment_task_id,
            'comment_text' : self.comment_text,
            'comment_time' : self.comment_time
        }

class Tag(models.Model):
    tag_id = models.AutoField('Идентификатор тэга', primary_key=True)
    tag_name = models.CharField('Название тэга', max_length=512)
    tag_code = models.CharField('Код тэга', max_length=512)

    def __str__(self):
        return f'''
            Tag:
                tag_id: {self.tag_id},
                tag_name: {self.tag_name},
                tag_code: {self.tag_code}
        '''
    
    def to_dict(self):
        return {
            'tag_id' : self.tag_id,
            'tag_name' : self.tag_name,
            'tag_code' : self.tag_code
        }

class TaskTags(models.Model):
    link_id = models.AutoField('Идентификатор связи', primary_key=True)
    link_task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='fk_link_tag_task')
    link_tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='fk_link_tag_tag')

    def __str__(self):
        return f'''
            TaskTags:
                link_id: {self.link_id},
                link_task_id: {self.link_task_id},
                link_tag_id: {self.link_tag_id}
        '''
    
    def to_dict(self):
        return {
            'link_id' : self.link_id,
            'link_task_id' : self.link_task_id,
            'link_tag_id' : self.link_tag_id
        }

