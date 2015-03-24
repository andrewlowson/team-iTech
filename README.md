# team-iTech
Group repository for Internet Technology


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

$ workon environmentname

(environmentname)$

The command 'lsvirtualenv' can be used if you have more than one virtual environment created

###Setup Database and Population Script


$ python manage.py syncdb // Setup the database

When creating superuser, do not create one called testuser, as this is hardcoded into the population script.

$ python manage.py migrate // Migrate changes to the database. Before this, you may have to run the 'python manage.py makemigrations' command first

$ python populate_fmk.py // Run the population script. You may need to run the migrate command again.

### Run Server

$ python manage.py runserver  // Run start the server and navigate to the home page at http://127.0.0.1:8000



————————————————————————————————————————————————————————————————————————————————————————————————————————-

###Application can be reached at: fmkitech.pythonanywhere.com

###Test Users Credentials: 

Username: testuser 

Password: testpass

###About The Application

This is a web application game that lets you choose from three celebrities who you would rather Fuck (F), Marry (M), or Kill (K). The random game is allowed to be played by all players, regardless of if they have an account with FMK or not. This game picks three celebrities at random, upon which the player can then select which one they would F, M or K.

If the player creates an account or is signed in, then they can access other features, as well as the random game. Create a game allows the player to pick three celebrities, rather than them being random, and share the game with friends, or play it themselves. 

The application also contains top tables that display the celebrities that have been fucked, married, and killed the most. The hall of shame table shows which users have played the game the most. 

Players that have accounts can also add celebrities to the game that are not already in the database by supplying their name and a photo of that celebrity, as well as giving them a defined category. If the category does not exit, the player may create it also, so it can be used my other players.

Players can also use dynamic search boxes to search for celebrities by categories in the create a game page, and in the add a celebrity page, so that the player can check if the celebrity already exists.

————————————————————————————————————————————————————————————————————————————————————————————————————————-
###Social Media 

Check FMK out on twitter at @fmkitech. The application contains twitter intergration, allowing the player to share the application, share their results of a game, and also share or send their created game with friends.

Find us at: 

https://twitter.com/search?q=%20%23fmkitech%20OR%20%40fmkitech&src=typd
Tweets about #fmkitech OR @fmkitech

