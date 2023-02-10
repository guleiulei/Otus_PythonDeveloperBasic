from django.db import models


no_epic_id = None


class Epic(models.Model):
    epic_name = models.CharField(max_length=64, )
    description = models.TextField(verbose_name='epic_description', null=True, blank=True)

    def __str__(self):
        return self.epic_name


class Task(models.Model):
    task_name = models.CharField(max_length=256)
    description = models.TextField(verbose_name='task_description', null=True, blank=True)
    # start_time = models.DateTimeField(auto_now_add=True)
    # end_time = models.DateTimeField(null=True, blank=True)
    hours = models.SmallIntegerField(default=0)
    minutes = models.IntegerField(default=0)
    epic = models.ForeignKey(Epic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.task_name}'


