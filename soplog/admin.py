from django.contrib import admin

# Register your models here.
from soplog.models import *

admin.site.register(Group)
admin.site.register(Checklist)
admin.site.register(ChecklistStep)
admin.site.register(StepType)