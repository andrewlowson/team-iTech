from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from fmk.models import Celebrity, Player, Game, Result, Category
from fmk.forms import SignUpForm, AddCategoryForm, AddCelebrityForm, CreateGameForm, ResultForm
from django.core.urlresolvers import reverse

import random


# No information is required from the models
# Simply returns the appropriate template
def index(request):
    return render(request, 'fmk/index.html')

def about(request):
    return render(request, 'fmk/about.html')

def contact_us(request):
    return render(request, 'fmk/contact_us.html')

def site_map(request):
    return render(request, 'fmk/site_map.html')


# View for creating a user account
def sign_up(request):
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)
        # Creates a User and Player objects with the given credentials
        if user_form.is_valid():
            user = user_form.save()
            password = user.password
            user.set_password(user.password)
            user.save()
            Player.objects.get_or_create(user=user)[0]
            username = user.username
            registered = True
            # The user is signed in automatically and returned to the index page
            player = authenticate(username=username, password=password)
            login(request, player)
            return HttpResponseRedirect(reverse('index'))
        else:
            print user_form.errors
    else:
        user_form = SignUpForm()
    return render(request,
                  'fmk/sign_up.html',
                  {'user_form': user_form, 'registered': registered})


# View for user sign in (login) page
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # If the user existes and has not been disabled then they are logged in and sent to the index page
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is currently disabled")
        else:
            print "Invalid Login Details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid Login Details Supplied")

    else:
        return render(request, 'fmk/sign_in.html')

# View to logout the user and return them to the index page
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
# The view which displays a random game 
# 3 random non-matching integers are chosen 
# A game is created and the celebrities with these integers as their ids are entered 
def random_game(request):
    form = ResultForm()
    celeb_list = []
    while (len(celeb_list)<3):
        random_idx = random.randint(0, Celebrity.objects.count()-1)
        celeb = Celebrity.objects.all()[random_idx]
        if celeb not in celeb_list:
            celeb_list.append(celeb)
    game = Game.objects.get_or_create(celebrity1 = celeb_list[0], celebrity2 = celeb_list[1], celebrity3=celeb_list[2])[0]
    context_dict = {
        'random_celebs': celeb_list,
        'form': form,
        'game': game,
    }
    Game.objects.get_or_create(celebrity1 = celeb_list[0], celebrity2 = celeb_list[1], celebrity3=celeb_list[2])
    return render(request, 'fmk/random_game.html', context_dict)

# The view which is run when the player submits their choices for a game
# For each of the three celebrities their appropriate counter will increase (F|M|K),
# the number of games that they have appeared in will increase and their stats will be returned
# If the player is logged in then these choices will be saved in a Result object that contains the player id as a foreign key
# If the player is logger in then their games played number will be increased
def playgame(request, gameID):
    context_dict = {'game':[], 'stats':[], 'celebrities':[]}
    game = Game.objects.get(id = gameID)
    celeb_id_list = [game.celebrity1, game.celebrity2, game.celebrity3]
    if request.method == 'POST':
        form = ResultForm(data=request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result_list = [result.result1, result.result2, result.result3]
            # For both registered and unregistered players the celebrity stats are changed
            for index in range(0, 3):
                celebrity = Celebrity.objects.get(id=celeb_id_list[index].id)
                numberGames = celebrity.num_results+1
                celebrity.num_results = numberGames
                if result_list[index]=='F':
                    fcount = celebrity.fuck_count
                    newFCount = fcount+1
                    celebrity.fuck_count = newFCount
                    celebrity.save()
                    stat_number = "{0:.0f}".format(round(float(newFCount)/numberGames*100, 2))
                    context_dict['stats'].append(str(stat_number)+'% of people fucked!')
                elif result_list[index]=='M':
                    mcount = celebrity.marry_count
                    newMCount = mcount+1
                    celebrity.marry_count=newMCount
                    celebrity.save()
                    stat_number = "{0:.0f}".format(round(float(newMCount)/numberGames*100, 2))
                    context_dict['stats'].append(str(stat_number)+'% of people married!')
                elif result_list[index]=='K':
                    kcount = celebrity.kill_count
                    newKCount = kcount+1
                    celebrity.kill_count=newKCount
                    celebrity.save()
                    stat_number = "{0:.0f}".format(round(float(newKCount)/numberGames*100, 2))
                    context_dict['stats'].append(str(stat_number)+'% of people killed!')
                if request.user.is_authenticated():
                    # The results are only stored in the database if the user is signed in
                    result.player = Player.objects.get(user=request.user)
                    result.game_name = game
                    result.save()
            # If the user is authenticated then their games played counter increases by 1
            if request.user.is_authenticated:
                game_player = Player.objects.get(user=request.user)
                play_count = game_player.gamesPlayed
                print play_count
                newPlayCount = play_count + 1
                game_player.gamesPlayed = newPlayCount
                print game_player.gamesPlayed
                game_player.save()
        else:
            print form.errors
            context_dict.update({'form': form})
    else:
        form = ResultForm()
        context_dict.update({'form': form})
    context_dict.update({'game': game})
    for index in range(0, 3):
            celebrity = Celebrity.objects.get(id=celeb_id_list[index].id)
            context_dict['celebrities'].append(celebrity)
    return render(request, 'fmk/playgame.html', context_dict)

# This view takens in information from the CreateGame form and stores it as a Game object
def add_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        # is the form valid?
        if form.is_valid():
            game = form.save(commit=True)
            game_id = game.id
            context_dict = {'game_id': game_id}
            return render(request, 'fmk/create_a_game.html', context_dict)
        else:
            print form.errors
    else:
        form = CreateGameForm()
        celeb_list = Celebrity.objects.all()
        context_dict = {
            'celebrities': celeb_list,
            'form': form,
        }
    return render(request, 'fmk/create_a_game.html', {'form': form})

# This view takes in the information from the AddCelebrity form and stores it as a Celebrity object
def add_celebrity(request):
    if request.method == 'POST':
        form = AddCelebrityForm(request.POST, request.FILES)
        if form.is_valid():
            celebrity = form.save(commit=False)
            if 'picture' in request.FILES:
                celebImage = request.FILES['picture']
                celebrity.picture = celebImage
                celebrity.save()
            celebrity.save()
            return index(request)
        else:
            print form.errors
    else:
        form = AddCelebrityForm()
        celeb_list = Celebrity.objects.all()
        context_dictionary = {
            'celebrities': celeb_list,
            'form': form,
        }
    return render(request, 'fmk/add_celebrity.html', context_dictionary)
  
# This view takes in the information from the AddCategory form and stores it as a Category object
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        # is the form valid?
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = AddCategoryForm()
    return render(request, 'fmk/add_category.html', {'form': form})


# Helper function to find all the celebrities starting with the name inputted
def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name_istartswith = starts_with)

    if max_results > 0:
            if len(cat_list) > max_results:
                    cat_list = cat_list[:max_results]

    return cat_list


# Retrieves the 5 celebrities who have been killed the most, married the most and fucked the most
# Also returns 5 players who have played it the most times
def top_tables(request):
    most_f_list = Celebrity.objects.order_by('-fuck_count')[:5]
    most_m_list = Celebrity.objects.order_by('-marry_count')[:5]
    most_k_list = Celebrity.objects.order_by('-kill_count')[:5]
    most_p_list = Player.objects.order_by('-gamesPlayed')[:5]
    context_dict = {
        'fuck_list': most_f_list,
        'marry_list': most_m_list,
        'kill_list': most_k_list,
        'plays_list': most_p_list,
        }

    return render(request, 'fmk/top_tables.html', context_dict)

