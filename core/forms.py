from django import forms
from .models import Task

#class
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','complete']