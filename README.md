# team-iTech
Group repository for Internet Technologies


##Contact Information

Andrew
0800685L@student.gla.ac.uk

Marco
2152599C@student.gla.ac.uk

Mary
1003254M@student.gla.ac.uk

Scott
2164953G@student.gla.ac.uk

## Setup

###Install Virtual Environment
install virtualenv and virtualenvwrapper

$ pip install virtualenv

$ pip install virtualenvwrapper

$ mkvirtualenv environmentname

###Install Requirements

See Requirements.txt for packages to install using the command 'pip install...'

###Work on Environment

$ workon rango

(rango)$

The command 'lsvirtualenv' can be used if you have more than one virtual environment created

###Setup Database and Population Script


$ python manage.py syncdb // Setup the database

$ python manage.py migrate // Migrate changes to the database. Before this, you may have to run the 'python manage.py makemigrations' command first

### Run Server

$ python manage.py runserver  // Run start the server and navigate to the home page at http://127.0.0.1:8000



——————————————————————————————————————————————————————————————————————————————————————————————————————--

###Application can be reached at: LINK

###Test User Credentials: ********

###About The Application

This is a web application game that lets you choose from three celebrities who you would rather Fuck 

(F), Marry (M), or Kill (K). The random game is allowed to be played by all players, regardless of if 

they have an account with FMK or not. This game picks three celebrities at random, upon which the 

player can then select which one they would F, M or K.

If the player creates an account or is signed in, then they can access other features, as well as the 

random game. Create a game allows the player to pick three celebrities, rather than them being 

random, and share the game with friends, or play it themselves. 
————————————————————————————————————————————————————————————————————————————————————————————————————————--
###Social Media

Check FMK out on twitter! The application contains twitter intergration, allowing the player to share the application, share their results of a game, and also share or send their created game with friends.

Find us at:

https://twitter.com/search?q=%20%23fmkitech%20OR%20%40fmkitech&src=typd
Tweets about #fmkitech OR @fmkitech

