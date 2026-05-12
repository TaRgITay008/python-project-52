from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Label

class LabelCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_label_creation(self):
        response = self.client.post(reverse('label_create'), {'name': 'срочно'})
        self.assertRedirects(response, reverse('labels_list'))
        self.assertTrue(Label.objects.filter(name='срочно').exists())

class LabelUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.label = Label.objects.create(name='старая')

    def test_label_update(self):
        response = self.client.post(
            reverse('label_update', args=[self.label.pk]),
            {'name': 'новая'}
        )
        self.assertRedirects(response, reverse('labels_list'))
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'новая')

class LabelDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.label = Label.objects.create(name='удаляемая')

    def test_label_delete(self):
        response = self.client.post(reverse('label_delete', args=[self.label.pk]))
        self.assertRedirects(response, reverse('labels_list'))
        self.assertFalse(Label.objects.filter(name='удаляемая').exists())
