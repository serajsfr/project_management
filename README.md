# Project Management App

## Setup

1. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
2. Run migrations
    ```sh
    python manage.py migrate
    ```
3. Create a superuser to log in
    ```sh
    python manage.py createsuperuser
    ```
4. Run the development server
    ```sh
    python manage.py runserver
    ```

## Access The Application

- UI: http://127.0.0.1:8000/
- API: http://127.0.0.1:8000/api/

## Usage

- UI Endpoints:
List tasks: /
Task detail: /tasks/<id>/
Create task: /tasks/create/
Update task: /tasks/<id>/edit/
Delete task: /tasks/<id>/delete/

- API Endpoints:
API login: /api/login/ (**Doesn't Work. Explained in project description.)
List and create tasks: /api/
Retrieve, update, delete task: /api/tasks/<id>/

## Bonus Tasks

- Tests are implemented in tests.py file.
- PythonAnywhere server: https://serajsafarian.pythonanywhere.com/

user1: username: seraj  password: 1234
user2: username: admin  password: 1234

## Project Description

This project implements a Task management system with both API and UI endpoints using Django and Django REST framework. Below are the key components and structure of the project:

Models
- Task Model: Defined in models.py, representing a task entity with relevant fields.
- There is a visual explanation of the model in project_management_edr file.

Forms and Serializers
- TaskForm: A form for creating and updating tasks.
- TaskSerializer: A serializer to convert the Task model instances to JSON for API responses and handle task creation and updates through the API.

Views
- TaskViewSet: A viewset for handling API requests related to tasks, providing endpoints for listing, creating, retrieving, updating, and deleting tasks.

- UI Views: Function-based views for handling the user interface, including task list, detail, create, update, and delete operations.

URL Configuration
- api/urls.py: Contains URL patterns for API endpoints, leveraging Django REST framework's router.
- /api/login/: This page doesn't support get method. If you use curl, you can see it works with
post method, instead.
write this command in your shell: 
curl -X POST -d "username=your_username&password=your_password" http://127.0.0.1:8000/api/login/
It will generate a token like this:
{
    "token": "your_api_token"
}
You can use the token to login through your shell:
curl -H "Authorization: Token your_api_token" http://127.0.0.1:8000/api/tasks/


- tasks/urls.py: Contains URL patterns for UI endpoints, ensuring a clean separation between API and UI routes for easier maintenance and modification.

Templates
- Login Template: Located in the registration folder within the templates directory, it handles the user login page.

- Task Templates: Located in the tasks folder within the templates directory, these templates extend base.html for a consistent layout across the application.

Settings
- settings.py: Configured with necessary settings for login URL, installed apps, and Django REST framework dependencies.