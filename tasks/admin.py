from django.contrib import admin
from .models import Task, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Category model.
    """
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin interface for Task model.
    """
    list_display = ('title', 'category', 'due_date', 'completed')
    list_filter = ('completed', 'category', 'due_date')
    search_fields = ('title', 'category__name')
    ordering = ('due_date',)
