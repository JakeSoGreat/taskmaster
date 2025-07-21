from django.db import models


class Category(models.Model):
    """
    A category model for organizing tasks.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    A simple task model for the taskmaster application.
    """
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
