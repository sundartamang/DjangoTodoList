from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,ListView,DetailView
from .models import Task
from django.contrib import messages
from .forms import TaskForm

# Create your views here.
class home(View):
    def get(self,*args, **kwargs):
        task = Task.objects.all()
        context = {
            'task':task
        }
        return render(self.request,'index.html',context)
    def post(self,*args, **kwargs):
        form = TaskForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(self.request,"Task has been successfully added")
            return redirect('/')
        else:
            messages.warning(self.request,"Somethign went wrong")
            return redirect('/')

def delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    messages.warning(request,"Task has been successfully deleted")
    return redirect('/')

def update(request,pk):
    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.info(request,"updated successfully")
            return redirect('/')
        else:
            messages.warning(request,"Something went wrong")
            return redirect('/')
    else:  
        task = Task.objects.get(id=pk)
        context = {
            'task':task
        }
        return render(request,'edit.html',context)


def cross(request,pk):
    task = Task.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect('/')

def uncross(request,pk):
    task = Task.objects.get(id=pk)
    task.complete = False
    task.save()
    return redirect('/')


