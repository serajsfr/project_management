from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(user=self.user, title='Test Task', description='Test Description')

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
