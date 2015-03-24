import unittest
from django.test import TestCase
from fmk.models import *
from fmk.views import *
from fmk.forms import *
from django.core.urlresolvers import reverse

# Test if that for a Player the gamesPlayed variable is positive
class PlayerModelTests(TestCase):
    def test_ensure_gamesPlayed_are_positive(self):
        # should result True for categories where gamesPlayer are greater or equal to zero
        user = User(username = 'testuser', email = 'test@gmail.com', password = 'testpass')
        player = Player(user = user)
        self.assertEqual((player.gamesPlayed>=0), True)

# Test the the model stores the entered strings correctly 
class CategoryModelTests(TestCase):
    def test_ensure_categories_can_be_added(self):
        #
        cat = Category(name = 'testCategory', description = 'This is a test category')
        self.assertEqual((cat.name=='testCategory' and cat.description=='This is a test category'), True)

# Test that for a newly added celebrity their F|M|K counters are set at zero
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

# Test that for three different celebrities can be successful added into a Game object
class GameModelTests(TestCase):
    def test_ensure_valid_game_can_be_created(self):
        cat = Category(name = 'testCategory', description = 'This is a test category')
        celeb1 = Celebrity(first_name='Test1', last_name ='Name', picture = 'test1.jpg', category = cat)
        celeb2 = Celebrity(first_name='Test2', last_name ='Name', picture = 'test2.jpg', category = cat)
        celeb3 = Celebrity(first_name='Test3', last_name ='Name', picture = 'test3.jpg', category = cat)
        game = Game(celebrity1=celeb1, celebrity2=celeb2, celebrity3=celeb3)
        self.assertEqual((game.celebrity1 == celeb1 and game.celebrity2 == celeb2 and game.celebrity3 == celeb3), True)

# Test that it is possible for 3 distinct user choices to be stored in a Result object
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

# Test that if there are celebrities present in the database then the top tables will rank them and return the ordered list
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

# Test that only three celebrities are selected for the random game
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

# Test that the PlayGame view works correctly given sample data
class PlayGameTests(TestCase):
    def test_basic_play_game_view(self):
        # define some basic data
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

        num_f_celeb3 = 7
        num_m_celeb3 = 20
        num_k_celeb3 = 100

        celeb3 = Celebrity(
            first_name='Test3',
            last_name ='Name',
            picture = 'test3.jpg',
            category = cat,
            fuck_count = num_f_celeb3,
            marry_count = num_m_celeb3,
            kill_count = num_k_celeb3,
        )
        celeb3.save()
        game = Game (celebrity1 = celeb1, celebrity2=celeb2, celebrity3=celeb3)
        game.save()

        # user visits the play game page, but not logged in
        #response = build_url('/play/', get ={'gameID':game})
        response = self.client.get(reverse('play_game', args=str(game.id)))
        self.assertEqual(response.status_code, 200)

        # check that 3 celebrities are returned
        num_celebs = len(response.context['celebrities'])
        self.assertEqual(num_celebs, 3)
        celeb_list = response.context['celebrities']
        # and that they are unique
        self.assertEqual((celeb_list[0]==celeb_list[1]), False)
        self.assertEqual((celeb_list[0]==celeb_list[2]), False)
        self.assertEqual((celeb_list[1]==celeb_list[2]), False)

        # check to ensure celebrity stats haven't been altered
        self.assertEqual((celeb_list[2].fuck_count==num_f_celeb3), True)
        self.assertEqual((celeb_list[2].marry_count==num_m_celeb3), True)
        self.assertEqual((celeb_list[2].kill_count==num_k_celeb3), True)

        # check a game is in the context dict
        self.assertEqual(response.context['game']!=None, True)

        # check a form is in the context dict
        self.assertEqual(response.context['form']!=None, True)


    def test_unauthenticated_results_post_view(self):
        # define some basic data
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

        num_f_celeb3 = 7
        num_m_celeb3 = 20
        num_k_celeb3 = 100

        celeb3 = Celebrity(
            first_name='Test3',
            last_name ='Name',
            picture = 'test3.jpg',
            category = cat,
            fuck_count = num_f_celeb3,
            marry_count = num_m_celeb3,
            kill_count = num_k_celeb3,
        )
        celeb3.save()
        game = Game (celebrity1 = celeb1, celebrity2=celeb2, celebrity3=celeb3)
        game.save()
        form = ResultForm()
        form.result1=u'F'
        form.result2=u'M'
        form.result3=u'K'

        # user visits the play game page, but not logged in
        response = reverse('play_game', args=str(game.id))
        response = self.client.post(response, {'result1':u'F', 'result2':u'M', 'result3':u'K'})
        self.assertEqual(response.status_code, 200)

        # check that 3 celebrities are returned
        num_celebs = len(response.context['celebrities'])
        self.assertEqual(num_celebs, 3)
        celeb_list = response.context['celebrities']
        # and that they are unique
        self.assertEqual((celeb_list[0]==celeb_list[1]), False)
        self.assertEqual((celeb_list[0]==celeb_list[2]), False)
        self.assertEqual((celeb_list[1]==celeb_list[2]), False)

        # check to ensure celebrity stats haven't been altered

        self.assertEqual((celeb_list[2].fuck_count==num_f_celeb3), True)
        self.assertEqual((celeb_list[2].marry_count==num_m_celeb3), True)
        self.assertEqual((celeb_list[2].kill_count==num_k_celeb3), False)

        # check a game is in the context dict
        self.assertEqual(response.context['game']!=None, True)

