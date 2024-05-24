from django.test import TestCase
from .forms import UserForm
from .models import UserInfo
from django.contrib.auth.models import User

# Create your tests here.
class Form(TestCase):

    def test_form_is_valid(self):
        userform = UserForm({'user': 'text text'})
        self.assertFalse(userform.is_valid())



class View(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
        username="myUsername",
        password="myPassword",
        email="test@test.com"
        )
        self.user_info = UserInfo(date = "1999-02-02", user = self.user)
        self.user_info.save()