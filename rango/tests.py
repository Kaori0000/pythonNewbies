from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client

# Create your tests here.

# Test if a user can log-in with password
class LoginTest(TestCase):

    def setUp(self):
        #Create a user
        user = User.objects.create_user(username='tester')
        user.set_password('tester123!')
        user.save()

    def test_login_correct_password(self):
        #test to see if it is possible to log in with a correct password
        c = Client()
        logged_in = c.login(username='tester', password='tester123!')
        self.assertTrue(logged_in)

    def test_login_wrong_password(self):
        #test to see if it is possible to log in with a incorrect password
        c = Client()
        logged_in = c.login(username='tester', password='wrong')
        self.assertFalse(logged_in)


# Test if the login page contains hyperlinks for users to register, reset password, and login with their GitHub account
class LoginPageViewTest(TestCase):
    def test_login_view_hyperlinks(self):
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        #check whether the page loaded successfully(with a 200 status code returned)
        self.assertContains(response, '<a href="%s">Register here!</a>' % reverse("registration_register"),html=True)
        #check if the login page contains a hyper link for register
        self.assertContains(response, '<a href="%s">Reset here!</a>' % reverse('auth_password_reset'),html=True)
        #check if the login page contains a hyper link for reset password
       # self.assertContains(response, '<a href="%s">Login with GitHub</a>' % reverse('social_django.urls'),html=True)
        #check if the login page contains a hyper link for logging in with GitHub account


