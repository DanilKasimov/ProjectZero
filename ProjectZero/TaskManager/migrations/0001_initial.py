# Generated by Django 4.2 on 2023-04-05 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('task_type_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификатор типа задачи')),
                ('task_type_name', models.CharField(max_length=512, verbose_name='Наименование типа задачи')),
                ('task_type_code', models.CharField(max_length=10, verbose_name='Код типа задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификатор задачи')),
                ('task_type_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TaskManager.tasktype')),
            ],
        ),
    ]
