from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserCreateTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('user_create'), {
            'username': 'newuser',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123',
        })
        # Проверяем редирект на страницу входа
        self.assertRedirects(response, reverse('login'))
        # Проверяем, что пользователь создался
        self.assertTrue(User.objects.filter(username='newuser').exists())

class UserUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='OldPass123'
        )

    def test_user_update(self):
        self.client.login(username='testuser', password='OldPass123')
        response = self.client.post(
            reverse('user_update', args=[self.user.pk]),
            {
                'first_name': 'NewName',
                'last_name': 'NewLastName',
                'username': 'testuser'
            }
        )
        self.assertRedirects(response, reverse('users_list'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'NewName')
        self.assertEqual(self.user.last_name, 'NewLastName')

class UserDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='todelete',
            password='DeletePass123'
        )

    def test_user_delete(self):
        self.client.login(username='todelete', password='DeletePass123')
        response = self.client.post(reverse('user_delete', args=[self.user.pk]))
        self.assertRedirects(response, reverse('users_list'))
        self.assertFalse(User.objects.filter(username='todelete').exists())
