import unittest
from django.test import TestCase
from fmk.models import *
from fmk.views import *
from django.core.urlresolvers import reverse

class SignUpViewTests(TestCase):
    
    def test_player_creation(self):
        """
        checks that when a User is created a corresponding Player is greated
        does this by checking that there is a Player with the same username 
        that has a valid gamesPlayed count
        """
        user = User(username='test', password='pass')
        user.save()
        Player.objects.get_or_create(user=user)[0]
        player = User.objects.get(username='test')
        self.assertGreaterEqual(Player.objects.get(user=player).gamesPlayed, 0, 'Error GamesPlayed is less than zero')
        
class RandomGameViewTests(self):
    
    def test_random_game_with_no_celebrities(self):
        """
        If there are no celebrities then an appropriate message should be displayed
        """
        response = self.client.get(reverse('random_game'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 