from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User





class TaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPass123!')


    def test_task_1(self):
        response = self.client.get(reverse('task-list'))
        self.assertNotEqual(response.status_code, 200)


    def test_task_2(self):
        self.client.login(username='testuser', password='TestPass123!')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200) 



