from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from statuses.models import Status
from .models import Task

class TaskCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.status = Status.objects.create(name='новый')

    def test_task_creation(self):
        response = self.client.post(reverse('task_create'), {
            'name': 'Тестовая задача',
            'description': 'Описание',
            'status': self.status.id,
            'executor': self.user.id,
        })
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertTrue(Task.objects.filter(name='Тестовая задача').exists())
        task = Task.objects.get(name='Тестовая задача')
        self.assertEqual(task.author, self.user)

class TaskUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.status = Status.objects.create(name='новый')
        self.task = Task.objects.create(
            name='Старая задача',
            description='Старое описание',
            status=self.status,
            author=self.user,
            executor=self.user,
        )

    def test_task_update(self):
        response = self.client.post(
            reverse('task_update', args=[self.task.pk]),
            {
                'name': 'Обновленная задача',
                'description': 'Новое описание',
                'status': self.status.id,
                'executor': self.user.id,
            }
        )
        self.assertRedirects(response, reverse('tasks_list'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Обновленная задача')
        self.assertEqual(self.task.description, 'Новое описание')

class TaskDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.status = Status.objects.create(name='новый')
        self.task = Task.objects.create(
            name='Удаляемая задача',
            description='Описание',
            status=self.status,
            author=self.user,
            executor=self.user,
        )

    def test_task_delete_by_author(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertFalse(Task.objects.filter(name='Удаляемая задача').exists())

    def test_task_delete_by_non_author(self):
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertTrue(Task.objects.filter(name='Удаляемая задача').exists())
