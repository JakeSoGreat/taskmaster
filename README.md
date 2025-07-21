# TaskMaster

A simple Django-based task management application that helps you organize and track your daily tasks.

## Features

-   User authentication (using Django's built-in admin)
-   Create, read, update, and delete tasks
-   Mark tasks as complete/incomplete
-   User-specific task management
-   Responsive Bootstrap UI
-   Admin interface for task management

## Project Structure

```
taskmaster/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── taskmaster/              # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── tasks/                   # Tasks app
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── forms.py             # Django forms
│   ├── models.py            # Database models
│   ├── tests.py             # Unit tests
│   ├── urls.py              # App URL configuration
│   └── views.py             # View functions
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── tasks/               # Task-specific templates
│       ├── home.html
│       ├── task_list.html
│       ├── task_form.html
│       └── task_confirm_delete.html
└── static/                  # Static files (CSS, JS, images)
    └── css/
        └── style.css        # Custom styles
```

## Setup Instructions

1. **Install Django** (if not already installed):

    ```bash
    pip install django
    ```

2. **Apply database migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Create a superuser account**:

    ```bash
    python manage.py createsuperuser
    ```

4. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    - Main application: http://127.0.0.1:8000/
    - Admin interface: http://127.0.0.1:8000/admin/

## Usage

1. **Login**: Use the admin login to access your tasks
2. **Create Tasks**: Click "Create New Task" to add a new task
3. **Manage Tasks**: View all your tasks on the task list page
4. **Update Tasks**: Click "Edit" to modify existing tasks
5. **Complete Tasks**: Click "Mark Complete" to mark tasks as done
6. **Delete Tasks**: Click "Delete" to remove tasks permanently

## Models

### Task Model

-   `title`: CharField - The task title (max 200 characters)
-   `description`: TextField - Optional task description
-   `completed`: BooleanField - Task completion status
-   `created_at`: DateTimeField - Timestamp when task was created
-   `updated_at`: DateTimeField - Timestamp when task was last updated
-   `user`: ForeignKey - Links task to a specific user

## Views

-   `home`: Welcome page with navigation links
-   `task_list`: Display all user's tasks
-   `task_create`: Create a new task
-   `task_update`: Edit an existing task
-   `task_delete`: Delete a task with confirmation
-   `task_toggle`: Toggle task completion status

## Templates

All templates extend the base template which includes:

-   Bootstrap 5 for responsive design
-   Navigation bar with user authentication status
-   Flash messages for user feedback
-   Custom CSS for enhanced styling

## Testing

Run the test suite:

```bash
python manage.py test
```

## Notes

-   This is a boilerplate Django project using only Django's built-in features
-   No third-party packages are used beyond Django itself
-   SQLite database is used by default (suitable for development)
-   Bootstrap is loaded via CDN for styling
-   User authentication is handled through Django's admin interface
