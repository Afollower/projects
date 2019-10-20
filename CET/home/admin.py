from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.exam_entry_table)    #考点信息表
admin.site.register(models.user_entry_table)    #用户考试信息表
admin.site.register(models.user_data)           #用户信息表