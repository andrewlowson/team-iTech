import unittest
from django.test import TestCase
from fmk.models import *
from fmk.views import *
from django.core.urlresolvers import reverse


class SignUpTest(unittest.TestCase):


    def SignUp(self):
        "I'm not sure what I'm doing"

        self.request = sign_up('andrewlowson', 'andrew@lowson.co', 'password')
        # self.form = SignUpForm(data=self.request.POST)
        # self.user = self.form.save()
        # self.password = self.user.password
        # self.user.set_password(self.user.password)
        # self.user.save()
        # Player.objects.get_or_create(user=self.user)[0]
        # self.username = self.user.username
        # registered=True
        # self.player = authenticate(username=self.username, password=self.password)


        self.assertEqual(username = 'andrewlowson')


    def SignIn(self):

        self.request = sign_in(self.username, self.password)

        self.assertEqual(HttpResponseRedirect,'/fmk/')



class OtherSignUp(unittest.TestCase):

    def FailTest(self):

        "HOping this fails"

        self.request = sign_up(123,123,123)

        assert HttpResponseRedirect == '/fmk/'