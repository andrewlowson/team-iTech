from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Use the default Django User model
# This provides the attributes: 
#	username
#	password
#	email
#	first_name
#	last_name

# The user object with the added attribute of a play counter
class Player(models.Model):
	user = models.OneToOneField(User)
	# The number of games that a player has played
	gamesPlayed = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return self.user.username

# The category object which is used to split the celebrity into their respective occupations 
# or defining characteristic
class Category(models.Model):
	name = models.CharField(max_length = 60, unique=True, primary_key=True)
	description = models.CharField(max_length = 300)
	
	def __unicode__(self):
		return self.name
		
# The Celebrity object contains the information about each of the celebrities in the game
# This includes the numbers that are required to find out the statistics relating to each celebrity
class Celebrity(models.Model):
	first_name = models.CharField(max_length = 60)
	last_name = models.CharField(max_length = 60)
	picture = models.ImageField(upload_to = 'FMK_Celebrity_Thumbs/')
	category = models.ForeignKey(Category, verbose_name='categories')
	# Keeps a record of how many times each celebrity has been F, M or K 
	fuck_count = models.IntegerField(default=0)
	marry_count = models.IntegerField(default=0)
	kill_count = models.IntegerField(default=0)
	# Keeps a record of how many times they have appeared in a game
	num_results = models.IntegerField(default=0)

	def __unicode__(self):
		return self.first_name+' '+self.last_name


# The Game object keeps a record of which three celebrities were involved in each game		
class Game(models.Model):
	celebrity1 = models.ForeignKey(Celebrity, related_name = 'first_celeb',)
	celebrity2 = models.ForeignKey(Celebrity, related_name = 'second_celeb',)
	celebrity3 = models.ForeignKey(Celebrity, related_name = 'third_celeb',)

	def __unicode__(self):
		return 'Game '+str(self.id)

# The Result object contains the players choices in terms of F, M or K
# These can then be related back to the appropriate celebrity as Game.celebrity1 received Result.result1 and so on
class Result(models.Model):
	game_name = models.ForeignKey(Game)
	player = models.ForeignKey(Player)
	OPTIONS = (
		('F', 'Fuck'),
		('M', 'Marry'),
		('K', 'Kill'),
	)
	result1 = models.CharField(max_length=1, choices = OPTIONS)
	result2 = models.CharField(max_length=1, choices = OPTIONS)
	result3 = models.CharField(max_length=1, choices = OPTIONS)

	def __unicode__(self):
		return str(self.game_name) + ' results'
