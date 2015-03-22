from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from fmk.models import Celebrity, Player, Game, Result
from fmk.forms import SignUpForm, AddCategoryForm, AddCelebrityForm, CreateGameForm, ResultForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
import random


def index(request):
    context_dict = {
        'boldmessage': "FMK will be awesome...eventually.",
    }

    return render(request, 'fmk/index.html', context_dict)


def about(request):
    return render(request, 'fmk/about.html')

def contact_us(request):
    return render(request, 'fmk/contact_us.html')

def site_map(request):
    return render(request, 'fmk/site_map.html')


def top_tables(request):
    most_f_list = Celebrity.objects.order_by('-fuck_count')[:5]
    most_m_list = Celebrity.objects.order_by('-marry_count')[:5]
    most_k_list = Celebrity.objects.order_by('-kill_count')[:5]
    context_dict = {
        'fuck_list': most_f_list,
        'marry_list': most_m_list,
        'kill_list': most_k_list,

        }

    return render(request, 'fmk/top_tables.html', context_dict)


def playgame(request, gameID):
    context_dict = {'game':[], 'stats':[], 'celebrities':[]}
    game = Game.objects.get(id = gameID)
    # context_dict['game'].append(game)
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
                context_dict['celebrities'].append(celebrity)
                if request.user.is_authenticated():
                    # The results are only stored in the database if the user is signed in
                    result.player = Player.objects.get(user=request.user)
                    result.game_name = game
                    result.save()
        else:
            print form.errors
    else:
        form = ResultForm()
        for index in range(0, 3):
            celebrity = Celebrity.objects.get(id=celeb_id_list[index].id)
            context_dict['celebrities'].append(celebrity)

    context_dict.update({'form': form})
    context_dict.update({'game': game})
    return render(request, 'fmk/playgame.html', context_dict)

# def user_stats(request):
#     context_dict = {
#         'boldmessage': "How does one retrieve the users fucked, married and killed? So many models and connections!",
#     }
# return render(request, 'fmk/index.html', context_dict)


# View for creating a user account
def sign_up(request):
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            Player.objects.get_or_create(user=user)[0]

            registered = True
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

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fmk/')
            else:
                return HttpResponse("Your account is currently disabled")
        else:
            print "Invalid Login Details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid Login Details Supplied")

    else:
        return render(request, 'fmk/sign_in.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/fmk/')

def add_category(request):
    # A HTTP POST?
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


def add_celebrity(request):
    # A HTTP POST?
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
    return render(request, 'fmk/add_celebrity.html', {'form': form})


def add_game(request):
    # A HTTP POST?
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
    return render(request, 'fmk/create_a_game.html', {'form': form})


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
        #'range': range(3)
    }
    Game.objects.get_or_create(celebrity1 = celeb_list[0], celebrity2 = celeb_list[1], celebrity3=celeb_list[2])
    return render(request, 'fmk/random_game.html', context_dict)

#def player_stats(request):
    #if request.user.is_authenticated():
        #player = Player.objects.get(user = request.user)
        #playerGames = Result.objects.select_related().filter(player=player)
        #print playerGames
        #for game in playerGames:
            #most_f_list = Celebrity.objects.select_related().filter(game_name=game)
        #print most_f_list


    #else:
        #return render(request, 'fmk/sign_in.html')


def stolen(request):

    return render(request, 'fmk/stolen.html')


# Helper function to find all the celebrities starting with the name inputted
def get_celebrity_list(max_results=0, starts_with=''):
    celebrity_list = []
    if starts_with:
        celebrity_list = Celebrity.objects.filter(Celebrity_name_startswith = starts_with)

    if max_results > 0:
            if len(celebrity_list) > max_results:
                    celebrity_list = celebrity_list[:max_results]

    for celebrity in celebrity_list:
        celebrity.url = Celebrity.first_name

    return celebrity_list



# View to examine the request and pick out the celebrity query string
def suggest_celebrity(request):
    celebrity_list = []
    starts_with = ''
    if request.method == 'GET':
            starts_with = request.GET['suggestion']
    celebrity_list = get_celebrity_list(5, starts_with)

    return render(request, 'fmk/celebrity_list.html', {'celebrity_list' : celebrity_list})
