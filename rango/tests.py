from django.http import response
from rango.models import UserProfile
from django.test import TestCase, testcases
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


# Test if the login page contains hyperlinks for users to register,and reset password
class LoginPageViewTest(TestCase):
    def test_login_view_hyperlinks(self):
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        #check whether the page loaded successfully(with a 200 status code returned)
        self.assertContains(response, '<a href="%s">Register here!</a>' % reverse("registration_register"),html=True)
        #check if the login page contains a hyper link for register
        self.assertContains(response, '<a href="%s">Reset here!</a>' % reverse('auth_password_reset'),html=True)
        #check if the login page contains a hyper link for reset password
       

     

class UserProfileUserNameTest(TestCase):
    #check if the user profile name matches the user's name
    def test_userProile_and_user(self):
    
        userA = User.objects.create_user(username='Alice')
        userA.set_password('userAlice123!')
        userA.save()

        userProfile = UserProfile(user=userA)
        userProfile.save()
        self.assertEqual(userProfile.user.username, userA.username) 

        
#check if the about us page has team member's pictures and contact informatin 
class AboutUsePageTest(TestCase):
    def test_about_us_page(self):
        response = self.client.get(reverse('rango:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'grace.jpg')
        self.assertContains(response,'kaori.jpg')
        self.assertContains(response,'su.jpg')
        self.assertContains(response,'yue.jpg')
        self.assertContains(response,'Contact Details')
        self.assertContains(response,'Glasgow, G12 8QQ, Scotland')
        self.assertContains(response,'cats@student.gla.ac.uk')



