from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        expense_user = get_user_model()
        user = expense_user.objects.create_user(
            username='normal@user.com',
            password='foo'
        )
        self.assertEqual(user.username, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # email is None for the AbstractUser option
            # email does not exist for the AbstractBaseUser option
            self.assertEqual(user.email, '')
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            expense_user.objects.create_user()
        with self.assertRaises(ValueError):
            expense_user.objects.create_user(username='')
        with self.assertRaises(ValueError):
            expense_user.objects.create_user(username='', password="foo")

    def test_create_superuser(self):
        expense_user = get_user_model()
        admin_user = expense_user.objects.create_superuser(
            username='super@user.com',
            password='foo'
        )
        self.assertEqual(admin_user.username, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertEqual(admin_user.email, '')
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            expense_user.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
