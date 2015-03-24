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
    # is the user currently registered
    registered = False
    # if the request if a 'POST'
    if request.method == 'POST':
        # Obtain the sign in form from the POST request
        user_form = SignUpForm(data=request.POST)
        # is the form valid?
        if user_form.is_valid():
            # if so, commit the changes to the database
            user = user_form.save()
            # retrieve unencrypted copy of password for automatic login
            password = user.password
            user.set_password(user.password)
            user.save()
            # for each registered user, a Player object must be generated
            Player.objects.get_or_create(user=user)[0]
            username = user.username
            registered = True
            # The user is signed in automatically and returned to the index page
            player = authenticate(username=username, password=password)
            login(request, player)
            return HttpResponseRedirect(reverse('index'))
        else:
            # if the form is invalid, display the errors to the user
            print user_form.errors
    else:
        # if the request method is not a 'POST'
        # create a new form
        user_form = SignUpForm()
    return render(request,
                  'fmk/sign_up.html',
                  {'user_form': user_form, 'registered': registered})


# View for user sign in (login) page
def sign_in(request):
    # is the request a 'POST'?
    if request.method == 'POST':
        # retrieve the username and password from the POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # If the user exists and has not been disabled then they are logged in and sent to the index page
            if user.is_active:
                login(request, user)
                # redirect the user to the index page
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is currently disabled")
        else:
            # display that login details were invalid
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
    # Generate a new form for the results
    form = ResultForm()
    # Create a list to store the randomly allocated celebrities
    celeb_list = []
    # Repeat until 3 celebrities have been selected
    while (len(celeb_list)<3):
        # generate a random index between 0 and the number of celebrities in the database
        random_idx = random.randint(0, Celebrity.objects.count()-1)
        # retrieve the random celebrity from the database
        celeb = Celebrity.objects.all()[random_idx]
        if celeb not in celeb_list:
            # if the celebrity does not already exist in the list of random celebrities,
            # then they may be added
            celeb_list.append(celeb)
    # With each random game created, store the game in the database
    game = Game.objects.get_or_create(celebrity1 = celeb_list[0], celebrity2 = celeb_list[1], celebrity3=celeb_list[2])[0]
    # The context dictionary contains the celebrities, the results form and the game object
    context_dict = {
        'random_celebs': celeb_list,
        'form': form,
        # The game is included so the user's results can be POSTed to the appropriate page
        'game': game,
    }
    return render(request, 'fmk/random_game.html', context_dict)

# The view which is run when the player submits their choices for a game
# For each of the three celebrities their appropriate counter will increase (F|M|K),
# the number of games that they have appeared in will increase and their stats will be returned
# If the player is logged in then these choices will be saved in a Result object that contains the player id as a foreign key
# If the player is logger in then their games played number will be increased
def playgame(request, gameID):
    # create keys in the context dictionary for the game, stats, tweets and celebrities
    context_dict = {'game':[], 'stats':[], 'celebrities':[], 'tweets':[]}
    # retrieve the game and celebrities from the parameter passed in the URL
    game = Game.objects.get(id = gameID)
    celeb_id_list = [game.celebrity1, game.celebrity2, game.celebrity3]
    # if the request method was a POST
    if request.method == 'POST':
        form = ResultForm(data=request.POST)
        # check that the form is valid
        if form.is_valid():
            # however, don't commit the results to the database
            result = form.save(commit=False)
            # retrieve the results from the form data
            result_list = [result.result1, result.result2, result.result3]
            # For both registered and unregistered players the celebrity stats are changed
            for index in range(0, 3):
                celebrity = Celebrity.objects.get(id=celeb_id_list[index].id)
                # increment the number of results associated with the celebrity
                numberGames = celebrity.num_results+1
                celebrity.num_results = numberGames
                # if the user f*cked the celebrity
                if result_list[index]=='F':
                    fcount = celebrity.fuck_count
                    # increment the celebrities f*ck count
                    newFCount = fcount+1
                    celebrity.fuck_count = newFCount
                    # save the updated Celebrity back to the database
                    celebrity.save()
                    # construct a string so the user can tweet their result
                    context_dict['tweets'].append(str(celebrity)+' (F)')
                    # determine how many other user agreed with their selection
                    stat_number = "{0:.0f}".format(round(float(newFCount)/numberGames*100, 2))
                    context_dict['stats'].append(str(stat_number)+'% of people fucked!')
                elif result_list[index]=='M':
                    mcount = celebrity.marry_count
                    # increment the celebrities marry count
                    newMCount = mcount+1
                    celebrity.marry_count=newMCount
                    # save the updated Celebrity back to the database
                    celebrity.save()
                    # construct a string so the user can tweet their result
                    context_dict['tweets'].append(str(celebrity)+' (M)')
                    # determine how many other user agreed with their selection
                    stat_number = "{0:.0f}".format(round(float(newMCount)/numberGames*100, 2))
                    context_dict['stats'].append(str(stat_number)+'% of people married!')
                elif result_list[index]=='K':
                    kcount = celebrity.kill_count
                    # increment the celebrities kill count
                    newKCount = kcount+1
                    celebrity.kill_count=newKCount
                    # save the updated Celebrity back to the database
                    celebrity.save()
                    # construct a string so the user can tweet their result
                    context_dict['tweets'].append(str(celebrity)+' (K)')
                    # determine how many other user agreed with their selection
                    stat_number = "{0:.0f}".format(round(float(newKCount)/numberGames*100, 2))
                    context_dict['stats'].append(str(stat_number)+'% of people killed!')
            if request.user.is_authenticated():
                # The results are only stored in the database if the user is signed in
                game_player = Player.objects.get(user=request.user)
                result.player = game_player
                result.game_name = game
                # commit the result to the database
                result.save()
                play_count = game_player.gamesPlayed
                newPlayCount = play_count + 1
                # increment the number of games the user has played
                game_player.gamesPlayed = newPlayCount
                game_player.save()
        else:
            # if the form is invalid, add the form the context dictionary
            context_dict.update({'form': form})
    else:
        # if not a POST, create a new results form for the user
        form = ResultForm()
        context_dict.update({'form': form})
    # the game is always added to the context dictionary
    context_dict.update({'game': game})
    # retrieve the celebrities associated with the game and add them to the context dictionary
    for index in range(0, 3):
            celebrity = Celebrity.objects.get(id=celeb_id_list[index].id)
            context_dict['celebrities'].append(celebrity)
    return render(request, 'fmk/playgame.html', context_dict)

# This view takes in information from the CreateGame form and stores it as a Game object
def add_game(request):
    # if the request method is a POST
    if request.method == 'POST':
        # retrieve the form from the POST
        form = CreateGameForm(request.POST)
        # is the form valid?
        if form.is_valid():
            # commit the form to the database
            game = form.save(commit=True)
            game_id = game.id
            # add the game to the context dictionary
            context_dict = {'game_id': game_id}
            return render(request, 'fmk/create_a_game.html', context_dict)
        else:
            # if the form is invalid, display the errors
            print form.errors
    else:
        # if not a POST request, then create a new game form
        form = CreateGameForm()
        celeb_list = Celebrity.objects.all()
        # add the celebrities and the form to the context dictionary
        context_dict = {
            'celebrities': celeb_list,
            'form': form,
        }
    return render(request, 'fmk/create_a_game.html', context_dict)

# This view takes in the information from the AddCelebrity form and stores it as a Celebrity object
def add_celebrity(request):
    # if the method is a POST
    if request.method == 'POST':
        # retrieve the form from the POST
        form = AddCelebrityForm(request.POST, request.FILES)
        if form.is_valid():
            # if the form is valid
            # create a celebrity from the form but don't commit to the database
            celebrity = form.save(commit=False)
            # ensure the image is added to the celebrity
            if 'picture' in request.FILES:
                celebImage = request.FILES['picture']
                celebrity.picture = celebImage
            # Commit the celebrity to the database
            celebrity.save()
            return index(request)
        else:
            # display any errors to the user
            print form.errors
    else:
        # if the request is not a POST, create a new form
        form = AddCelebrityForm()
        celeb_list = Celebrity.objects.all()
        # add the form and the celebrities to the context dictionary
        context_dictionary = {
            'celebrities': celeb_list,
            'form': form,
        }
    return render(request, 'fmk/add_celebrity.html', context_dictionary)
  
# This view takes in the information from the AddCategory form and stores it as a Category object
def add_category(request):
    # if the request is a POST
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        # is the form valid?
        if form.is_valid():
            # save the form and save to database if valid
            form.save(commit=True)
            return index(request)
        else:
            # display the errors to the user
            print form.errors
    else:
        # if not a post then create a new category form
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
    # query the database for the most f,m and k'd celebrities
    # also query for the players with the most number of games played
    most_f_list = Celebrity.objects.order_by('-fuck_count')[:5]
    most_m_list = Celebrity.objects.order_by('-marry_count')[:5]
    most_k_list = Celebrity.objects.order_by('-kill_count')[:5]
    most_p_list = Player.objects.order_by('-gamesPlayed')[:5]
    # add the lists to the context dictionary
    context_dict = {
        'fuck_list': most_f_list,
        'marry_list': most_m_list,
        'kill_list': most_k_list,
        'plays_list': most_p_list,
        }

    return render(request, 'fmk/top_tables.html', context_dict)

