from django.test import TestCase
from .models import Task, Category
from datetime import date, timedelta


class CategoryModelTest(TestCase):
    """
    Test cases for the Category model.
    """
    def setUp(self):
        self.category = Category.objects.create(name='Work')

    def test_category_creation(self):
        """Test that a category is created correctly."""
        self.assertEqual(self.category.name, 'Work')

    def test_category_str_method(self):
        """Test the string representation of the category."""
        self.assertEqual(str(self.category), 'Work')


class TaskModelTest(TestCase):
    """
    Test cases for the Task model.
    """
    def setUp(self):
        self.category = Category.objects.create(name='Work')
        self.task = Task.objects.create(
            title='Test Task',
            due_date=date.today() + timedelta(days=7),
            category=self.category
        )

    def test_task_creation(self):
        """Test that a task is created correctly."""
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.category, self.category)
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.due_date, date.today() + timedelta(days=7))

    def test_task_str_method(self):
        """Test the string representation of the task."""
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_ordering(self):
        """Test that tasks are ordered by due date."""
        task2 = Task.objects.create(
            title='Urgent Task',
            due_date=date.today() + timedelta(days=1),
            category=self.category
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)  # Earlier due date first
        self.assertEqual(tasks[1], self.task)

    def test_task_without_category(self):
        """Test that a task can be created without a category."""
        task_no_cat = Task.objects.create(
            title='No Category Task',
            due_date=date.today()
        )
        self.assertIsNone(task_no_cat.category)
