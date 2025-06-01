from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task





class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPass123!')
        self.task = Task.objects.create(user = self.user, title = 'Test Task')



    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.user.username, 'testuser')