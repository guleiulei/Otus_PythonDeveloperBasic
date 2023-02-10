from django.contrib import admin
from tracker.models import Task, Epic


admin.site.register([Epic, Task])
