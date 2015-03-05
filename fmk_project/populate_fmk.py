import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fmk_project.settings')
# is the fmk_project.settings the correct variable

import django
django.setup()

from fmk.models import Player, Category, Celebrity, Game, Result
from fmk_project.settings import STATIC_CELEB_IMAGES_PATH

def populate():
    python_cat = add_category(
        name = 'Music',
        description = 'Famous celebrities from the world of music'
    )

    python_celeb = add_celeb(
        id = 1,
        fname = 'Kanye',
        sname = 'West',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 2,
        fname = 'Beyonce',
        sname = 'Knowles',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 3,
        fname = 'Taylor',
        sname = 'Swift',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 4,
        fname = 'Tom',
        sname = 'Delonge',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 5,
        fname = 'Justin',
        sname = 'Bieber',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 6,
        fname = 'Britney',
        sname = 'Spears',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 7,
        fname = 'Lady',
        sname = 'Gaga',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 8,
        fname = 'Katy',
        sname = 'Perry',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 9,
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
        id = 10,
        fname = 'Leonardo',
        sname = 'DiCaprio',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 11,
        fname = 'Robert',
        sname = 'Downey Jr.',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 12,
        fname = 'Tom',
        sname = 'Cruise',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 13,
        fname = 'Johnny',
        sname = 'Depp',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 14,
        fname = 'George',
        sname = 'Clooney',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 15,
        fname = 'Brad',
        sname = 'Pitt',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 16,
        fname = 'Jennifer',
        sname = 'Lawrence',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 17,
        fname = 'Emma',
        sname = 'Stone',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 18,
        fname = 'Kristen',
        sname = 'Stewart',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 19,
        fname = 'Anne',
        sname = 'Hathaway',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 20,
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
        id = 21,
        fname = 'Barack',
        sname = 'Obama',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 22,
        fname = 'Winston',
        sname = 'Churchill.',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 23,
        fname = 'Adolf',
        sname = 'Hitler',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 24,
        fname = 'Bill',
        sname = 'Clinton',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 25,
        fname = 'Margaret',
        sname = 'Thatcher',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 26,
        fname = 'Mahatma',
        sname = 'Gandhi',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 27,
        fname = 'Hilary',
        sname = 'Clinton',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 28,
        fname = 'Sarah',
        sname = 'Palin',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 29,
        fname = 'Angela',
        sname = 'Merkel',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 30,
        fname = 'Fidel',
        sname = 'Castro',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 31,
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
        id = 32,
        fname = 'Idris',
        sname = 'Elba',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 33,
        fname = 'Andrew',
        sname = 'Lincoln',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 34,
        fname = 'Hugh',
        sname = 'Laurie',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 35,
        fname = 'Lena',
        sname = 'Headey',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 36,
        fname = 'Cat',
        sname = 'Deeley',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 37,
        fname = 'Big',
        sname = 'Bird',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 38,
        fname = 'Susanna',
        sname = 'Reid',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 39,
        fname = 'Amanda',
        sname = 'Holden',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 40,
        fname = 'Rachel',
        sname = 'Riley',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

    python_celeb = add_celeb(
        id = 41,
        fname = 'Holly',
        sname = 'Willoughby',
        cat = python_cat,
        fcount = 0,
        mcount = 0,
        kcount = 0,
    )

def add_celeb(id, fname, sname, cat, fcount, mcount, kcount):
    picture_dir = str(id)+'.jpg'
    celeb = Celebrity.objects.get_or_create(
        celeb_id = id,
        first_name=fname,
        last_name=sname,
        category = cat,
        picture= os.path.join(STATIC_CELEB_IMAGES_PATH, picture_dir),
        fuck_count = fcount,
        marry_count = mcount,
        kill_count = kcount,
    )
    return celeb

def add_game(id, creator, celeb1, celeb2, celeb3, date):
    game= Game.objects.get_or_create(
        game_ID = id,
        creator = creator,
        celebrity1 = celeb1,
        celebrity2 = celeb2,
        celebrity3 = celeb3,
        date_created = date,
    )
    return game

def add_category(name, description):
    cat = Category.objects.get_or_create(name=name, description=description)[0]
    return cat

# Execution starts here
if __name__=='__main__':
    print "Starting fmk population script..."
    populate()