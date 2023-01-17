from django.db import models
no_epic_id = 1


class Epic(models.Model):
    epic_name = models.CharField(max_length=64)
    description = models.TextField(verbose_name='epic_description', null=True, blank=True)


class Task(models.Model):
    task_name = models.CharField(max_length=256)
    description = models.TextField(verbose_name='task_description', null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hours = models.SmallIntegerField(default=0)
    minutes = models.IntegerField(default=0)
    epic = models.ForeignKey(Epic, on_delete=models.SET_DEFAULT, default=no_epic_id)
