from django.contrib import admin
from .models import Task



# Register your models here.
#TODO try StackInLine and TaularInLine
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title','complete'
    )
    list_display_links = (
        'complete',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title','complete'
    )

    def combine(self,obj):
        return "{} - {}".format(obj.title, obj.complete)

admin.site.register(Task, TaskAdmin)