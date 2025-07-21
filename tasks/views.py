from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Task


def home(request):
    """
    Home view that redirects to admin or shows basic info.
    """
    return HttpResponse("""
    <h1>TaskMaster - Backend Only</h1>
    <p>Welcome to TaskMaster! The frontend templates have been removed.</p>
    <p>Please use the Django admin interface to manage tasks:</p>
    <p><a href="/admin/">Go to Admin Interface</a></p>
    """)


def task_list(request):
    """
    Redirect to admin task list.
    """
    return redirect('/admin/tasks/task/')


def task_create(request):
    """
    Redirect to admin task creation.
    """
    return redirect('/admin/tasks/task/add/')


def task_update(request, pk):
    """
    Redirect to admin task update.
    """
    return redirect(f'/admin/tasks/task/{pk}/change/')


def task_delete(request, pk):
    """
    Redirect to admin task deletion.
    """
    return redirect(f'/admin/tasks/task/{pk}/delete/')


def task_toggle(request, pk):
    """
    Toggle task completion status and redirect back.
    """
    try:
        task = Task.objects.get(pk=pk)
        task.completed = not task.completed
        task.save()
        return redirect('/admin/tasks/task/')
    except Task.DoesNotExist:
        return redirect('/admin/tasks/task/')
