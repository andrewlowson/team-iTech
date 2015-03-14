import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fmk_project.settings')
# is the fmk_project.settings the correct variable

import django
django.setup()

from fmk.models import Player, Category, Celebrity, Game, Result
from django.contrib.auth.models import User
from fmk_project.settings import STATIC_CELEB_IMAGES_PATH

def populate():

    python_user = User.objects.create_user(
        'testuser',
        'testuser@gmail.com',
        'testpass',
    )

    python_player = add_player(
        user = python_user
    )

    python_cat = add_category(
        name = 'Music',
        description = 'Famous celebrities from the world of music'
    )

    python_celeb = add_celeb(
        fname = 'Kanye',
        sname = 'West',
        cat = python_cat,
        fcount = 10,
        mcount = 20,
        kcount = 100,
    )

    python_celeb = add_celeb(
        fname = 'Beyonce',
        sname = 'Knowles',
        cat = python_cat,
        fcount = 30,
        mcount = 50,
        kcount = 4,
    )

    python_celeb = add_celeb(
        fname = 'Taylor',
        sname = 'Swift',
        cat = python_cat,
        fcount = 50,
        mcount = 70,
        kcount = 10,
    )

    python_celeb = add_celeb(
        fname = 'Tom',
        sname = 'Delonge',
        cat = python_cat,
        fcount = 20,
        mcount = 40,
        kcount = 1,
    )

    python_celeb = add_celeb(
        fname = 'Justin',
        sname = 'Bieber',
        cat = python_cat,
        fcount = 3,
        mcount = 10,
        kcount = 70,
    )

    python_celeb = add_celeb(
        fname = 'Britney',
        sname = 'Spears',
        cat = python_cat,
        fcount = 40,
        mcount = 30,
        kcount = 50,
    )

    python_celeb = add_celeb(
        fname = 'Lady',
        sname = 'Gaga',
        cat = python_cat,
        fcount = 40,
        mcount = 5,
        kcount = 55,
    )

    python_celeb = add_celeb(
        fname = 'Katy',
        sname = 'Perry',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Miley',
        sname = 'Cyrus',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_cat = add_category(
        name='Film',
        description = 'Actors, actresses and directors from the big screen'
    )

    python_celeb = add_celeb(
        fname = 'Leonardo',
        sname = 'DiCaprio',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Robert',
        sname = 'Downey Jr.',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Tom',
        sname = 'Cruise',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Johnny',
        sname = 'Depp',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'George',
        sname = 'Clooney',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Brad',
        sname = 'Pitt',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Jennifer',
        sname = 'Lawrence',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Emma',
        sname = 'Stone',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Kristen',
        sname = 'Stewart',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Anne',
        sname = 'Hathaway',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Sandra',
        sname = 'Bullock',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_cat = add_category(
        name='World Leader',
        description = 'Famous politicians, monarchs and dictators from around the globe'
    )

    python_celeb = add_celeb(
        fname = 'Barack',
        sname = 'Obama',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Winston',
        sname = 'Churchill.',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Adolf',
        sname = 'Hitler',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Bill',
        sname = 'Clinton',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Margaret',
        sname = 'Thatcher',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Mahatma',
        sname = 'Gandhi',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Hilary',
        sname = 'Clinton',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Sarah',
        sname = 'Palin',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Angela',
        sname = 'Merkel',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Fidel',
        sname = 'Castro',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'David',
        sname = 'Cameron',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_cat = add_category(
        name='TV',
        description = 'Celebrities from the small screen'
    )

    python_celeb = add_celeb(
        fname = 'Idris',
        sname = 'Elba',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Andrew',
        sname = 'Lincoln',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Hugh',
        sname = 'Laurie',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Lena',
        sname = 'Headey',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Cat',
        sname = 'Deeley',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Big',
        sname = 'Bird',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        fname = 'Susanna',
        sname = 'Reid',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb1 = add_celeb(
        fname = 'Amanda',
        sname = 'Holden',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb2 = add_celeb(
        fname = 'Rachel',
        sname = 'Riley',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb3 = add_celeb(
        fname = 'Holly',
        sname = 'Willoughby',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_game = add_game(
        celeb1=python_celeb1,
        celeb2=python_celeb2,
        celeb3=python_celeb3,
    )

    python_result = add_result(
        game = python_game,
        player = python_player,
        result1 = 'F',
        result2 = 'M',
        result3 = 'K',
    )


def add_player(user):
    player = Player.objects.get_or_create(
        user=user
    )[0]
    return player

def add_celeb(fname, sname, cat, fcount, mcount, kcount):
    picture_dir = fname+sname+'.jpg'
    celeb = Celebrity.objects.get_or_create(
        first_name=fname,
        last_name=sname,
        category = cat,
        picture= os.path.join(STATIC_CELEB_IMAGES_PATH, picture_dir),
        fuck_count = fcount,
        marry_count = mcount,
        kill_count = kcount,
    )[0]
    return celeb

def add_game(celeb1, celeb2, celeb3):
    game= Game.objects.get_or_create(
        celebrity1 = celeb1,
        celebrity2 = celeb2,
        celebrity3 = celeb3,
    )[0]
    return game

def add_category(name, description):
    cat = Category.objects.get_or_create(
        name = name,
        description = description
    )[0]
    return cat

def add_result(game, player, result1, result2, result3):
    result = Result.objects.get_or_create(
        game_name = game,
        player = player,
        result1 = result1,
        result2 = result2,
        result3 = result3,
    )[0]
    return result

# Execution starts here
if __name__=='__main__':
    print "Starting fmk population script..."
    populate()