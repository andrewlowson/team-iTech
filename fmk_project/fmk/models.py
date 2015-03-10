from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ValidationError

# Use the default Django User model
# This provides the attributes: 
#	username
#	password
#	email
#	first_name
#	last_name


class Player(models.Model):
	user = models.OneToOneField(User)
	
	# If we want to add more attributes for the players insert them here
	
	def __unicode__(self):
		return self.user.username
		
class Category(models.Model):
	name = models.CharField(max_length = 60, unique=True, primary_key=True)
	description = models.CharField(max_length = 300)
	
	def __unicode__(self):
		return self.name
		
class Celebrity(models.Model):
	celeb_id = models.IntegerField(max_length = 30, unique=True, primary_key=True)
	first_name = models.CharField(max_length = 60)
	last_name = models.CharField(max_length = 60)
	picture = models.ImageField(upload_to = 'celebrity_images', blank=True)
	category = models.ForeignKey(Category, verbose_name='categories')
	fuck_count = models.IntegerField(default=0)
	marry_count = models.IntegerField(default=0)
	kill_count = models.IntegerField(default=0)

	def __unicode__(self):
		return self.first_name+' '+self.last_name
		
class Game(models.Model):
	game_id = models.IntegerField(max_length = 30, unique = True, primary_key = True)
	creator = models.ForeignKey(Player)
	celebrity1 = models.ForeignKey(Celebrity, related_name = 'first_celeb',)
	celebrity2 = models.ForeignKey(Celebrity, related_name = 'second_celeb',)
	celebrity3 = models.ForeignKey(Celebrity, related_name = 'third_celeb',)
	date_created = models.DateField(blank=False, default=datetime.now())

	def __unicode__(self):
		return 'Game '+str(self.game_id)+' '+str(self.date_created)

class Result(models.Model):
	game_id = models.ForeignKey(Game)
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
		return str(self.game_id) + ' results'
