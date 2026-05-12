from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from statuses.models import Status
from .models import Task
from labels.models import Label

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

class TaskFilterTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass')
        self.other = User.objects.create_user(username='user2', password='pass')
        self.status = Status.objects.create(name='новый')
        self.label = Label.objects.create(name='важно')
        self.client.login(username='user1', password='pass')
        
        self.task1 = Task.objects.create(
            name='Моя задача',
            status=self.status,
            author=self.user,
            executor=self.user
        )
        self.task1.labels.add(self.label)
        
        self.task2 = Task.objects.create(
            name='Чужая задача',
            status=self.status,
            author=self.other
        )

    def test_filter_by_own_tasks(self):
        response = self.client.get(reverse('tasks_list'), {'only_self_tasks': 'on'})
        self.assertEqual(len(response.context['tasks']), 1)
        self.assertEqual(response.context['tasks'][0].name, 'Моя задача')

    def test_filter_by_status(self):
        response = self.client.get(reverse('tasks_list'), {'status': self.status.id})
        self.assertEqual(len(response.context['tasks']), 2)  # обе задачи с этим статусом

    def test_filter_by_label(self):
        response = self.client.get(reverse('tasks_list'), {'labels': self.label.id})
        self.assertEqual(len(response.context['tasks']), 1)
        self.assertEqual(response.context['tasks'][0].name, 'Моя задача')
