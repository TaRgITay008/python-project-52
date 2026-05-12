from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Status

class StatusCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_status_creation(self):
        response = self.client.post(reverse('status_create'), {'name': 'новый'})
        self.assertRedirects(response, reverse('statuses_list'))
        self.assertTrue(Status.objects.filter(name='новый').exists())

class StatusUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.status = Status.objects.create(name='старый')

    def test_status_update(self):
        response = self.client.post(
            reverse('status_update', args=[self.status.pk]),
            {'name': 'обновленный'}
        )
        self.assertRedirects(response, reverse('statuses_list'))
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'обновленный')

class StatusDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.status = Status.objects.create(name='удаляемый')

    def test_status_delete(self):
        response = self.client.post(reverse('status_delete', args=[self.status.pk]))
        self.assertRedirects(response, reverse('statuses_list'))
        self.assertFalse(Status.objects.filter(name='удаляемый').exists())
