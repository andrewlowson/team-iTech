import unittest
from django.test import TestCase
from fmk.models import *
from fmk.views import *
from django.core.urlresolvers import reverse


class PlayerModelTests(TestCase):
    def test_ensure_gamesPlayed_are_positive(self):
        # should result True for categories where gamesPlayer are greater or equal to zero
        user = User(username = 'testuser', email = 'test@gmail.com', password = 'testpass')
        player = Player(user = user)
        self.assertEqual((player.gamesPlayed>=0), True)


class CategoryModelTests(TestCase):
    def test_ensure_categories_can_be_added(self):
        #
        cat = Category(name = 'testCategory', description = 'This is a test category')
        self.assertEqual((cat.name=='testCategory' and cat.description=='This is a test category'), True)


class CelebrityModelTests(TestCase):
    def test_ensure_celebs_can_be_added(self):
        cat = Category(name = 'testCategory', description = 'This is a test category')
        celeb = Celebrity(
            first_name='John',
            last_name ='Travolta',
            picture = 'JohnTravolta.jpg',
            category = cat,
        )
        self.assertEqual((celeb.fuck_count==0 and celeb.marry_count==0 and celeb.kill_count==0), True)


class GameModelTests(TestCase):
    def test_ensure_valid_game_can_be_created(self):
        cat = Category(name = 'testCategory', description = 'This is a test category')
        celeb1 = Celebrity(first_name='Test1', last_name ='Name', picture = 'test1.jpg', category = cat)
        celeb2 = Celebrity(first_name='Test2', last_name ='Name', picture = 'test2.jpg', category = cat)
        celeb3 = Celebrity(first_name='Test3', last_name ='Name', picture = 'test3.jpg', category = cat)
        game = Game(celebrity1=celeb1, celebrity2=celeb2, celebrity3=celeb3)
        self.assertEqual((game.celebrity1 == celeb1 and game.celebrity2 == celeb2 and game.celebrity3 == celeb3), True)


class ResultModelTests(TestCase):
    def test_ensure_results_can_be_created(self):
        user = User(username = 'testuser', email = 'test@gmail.com', password = 'testpass')
        player = Player(user = user)
        cat = Category(name = 'testCategory', description = 'This is a test category')
        celeb1 = Celebrity(first_name='Test1', last_name ='Name', picture = 'test1.jpg', category = cat)
        celeb2 = Celebrity(first_name='Test2', last_name ='Name', picture = 'test2.jpg', category = cat)
        celeb3 = Celebrity(first_name='Test3', last_name ='Name', picture = 'test3.jpg', category = cat)
        game = Game (celebrity1 = celeb1, celebrity2=celeb2, celebrity3=celeb3)
        result = Result(
            game_name = game,
            player = player,
            result1 = 'F',
            result2 = 'M',
            result3 = 'K',
        )
        self.assertEqual((result.result1=='F' and result.result2=='M' and result.result3=='K'), True)

class TopTablesViewTests(TestCase):
    def test_top_tables_view(self):

        cat = Category(name = 'testCategory', description = 'This is a test category')
        cat.save()
        celeb1 = Celebrity(
            first_name='Test1',
            last_name ='Name',
            picture = 'test1.jpg',
            category = cat,
            fuck_count = 3,
            marry_count = 2,
            kill_count = 1,
        )
        celeb1.save()
        celeb2 = Celebrity(
            first_name='Test2',
            last_name ='Name',
            picture = 'test2.jpg',
            category = cat,
            fuck_count = 2,
            marry_count = 1,
            kill_count = 3,
        )
        celeb2.save()
        celeb3 = Celebrity(
            first_name='Test3',
            last_name ='Name',
            picture = 'test3.jpg',
            category = cat,
            fuck_count = 1,
            marry_count = 3,
            kill_count = 2,
        )
        celeb3.save()

        response = self.client.get(reverse('top_tables'))
        self.assertEqual(response.status_code, 200)
        num_celebs = len(response.context['fuck_list'])
        self.assertEqual(num_celebs, 3)
        num_celebs = len(response.context['marry_list'])
        self.assertEqual(num_celebs, 3)
        num_celebs = len(response.context['kill_list'])
        self.assertEqual(num_celebs, 3)


class RandomGameTest(TestCase):
    def test_random_game(self):
        cat = Category(name = 'testCategory', description = 'This is a test category')
        cat.save()
        celeb1 = Celebrity(
            first_name='Test1',
            last_name ='Name',
            picture = 'test1.jpg',
            category = cat,
            fuck_count = 3,
            marry_count = 2,
            kill_count = 1,
        )
        celeb1.save()
        celeb2 = Celebrity(
            first_name='Test2',
            last_name ='Name',
            picture = 'test2.jpg',
            category = cat,
            fuck_count = 2,
            marry_count = 1,
            kill_count = 3,
        )
        celeb2.save()
        celeb3 = Celebrity(
            first_name='Test3',
            last_name ='Name',
            picture = 'test3.jpg',
            category = cat,
            fuck_count = 1,
            marry_count = 3,
            kill_count = 2,
        )
        celeb3.save()
        celeb4 = Celebrity(
            first_name='Test4',
            last_name ='Name',
            picture = 'test4.jpg',
            category = cat,
            fuck_count = 1,
            marry_count = 3,
            kill_count = 2,
        )
        celeb4.save()

        response = self.client.get(reverse('random_game'))
        self.assertEqual(response.status_code, 200)
        num_celebs = len(response.context['random_celebs'])
        self.assertEqual(num_celebs, 3)
        celeb_list = response.context['random_celebs']
        self.assertEqual((celeb_list[0]==celeb_list[1]), False)
        self.assertEqual((celeb_list[0]==celeb_list[2]), False)
        self.assertEqual((celeb_list[1]==celeb_list[2]), False)














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