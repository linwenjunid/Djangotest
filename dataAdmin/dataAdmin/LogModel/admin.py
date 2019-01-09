from django.contrib import admin
from .models import Logs

class NewLog(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('IP','username'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('operate',),
        }]
    )
# Register your models here.
admin.site.register(Logs,NewLog)