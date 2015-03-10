from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from fmk.models import Celebrity, Player, Game
from fmk.forms import SignUpForm, AddCategoryForm, AddCelebrityForm, CreateGameForm, ResultForm
from django.contrib.auth import authenticate, login


def index(request):
    context_dict = {
        'boldmessage': "FMK will be awesome...eventually.",  
    }

    return render(request, 'fmk/index.html', context_dict)


def about(request):

    return render(request, 'fmk/about.html')


def top_tables(request):
    most_f_list = Celebrity.objects.order_by('-fuck_count')[:10]
    most_m_list = Celebrity.objects.order_by('-marry_count')[:10]
    most_k_list = Celebrity.objects.order_by('-kill_count')[:10]
    context_dict = {
        'fuck_list': most_f_list,
        'marry_list': most_m_list,
        'kill_list': most_k_list,
        }
    return render(request, 'fmk/top_tables.html', context_dict)


def play(request):
    top_fucked = Celebrity.objects.order_by('-fuck_count')[:1].get()
    top_married = Celebrity.objects.order_by('-marry_count')[:1].get()
    top_killed = Celebrity.objects.order_by('-kill_count')[:1].get()

    context_dict = {
        'week_fuck': top_fucked,
        'week_marry': top_married,
        'week_kill': top_killed,
    }

    return render(request, 'fmk/play.html', context_dict)


def create_game(request):
    context_dict = {
        'boldmessage': "JQuery magic goes here I believe.",
    }

    return render(request, 'fmk/create_game.html', context_dict)


def random_game(request):
    # random_celebrity1
    # random_celebrity2
    # random_celebrity3

    # Using these for now
    top_fucked = Celebrity.objects.order_by('-fuck_count')[:1].get()
    top_married = Celebrity.objects.order_by('-marry_count')[:1].get()
    top_killed = Celebrity.objects.order_by('-kill_count')[:1].get()
    context_dict = {
        'random_celeb1': top_fucked,
        'random_celeb2': top_married,
        'random_celeb3': top_killed,
    }

    return render(request, 'fmk/random_game.html', context_dict)


def user_stats(request):

    context_dict = {
        'boldmessage': "How does one retrieve the users fucked, married and killed? So many models and connections!",
        }

    return render(request, 'fmk/index.html', context_dict)


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
        form = AddCelebrityForm(request.POST)

        # is the form valid?
        if form.is_valid():
            form.save(commit=True)
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
            game = form.save(commit=False)
            creator = request.user
            game.creator = Player.objects.get(user=creator)
            game.save()

            return index(request)
        else:
            print form.errors
    else:
        form = CreateGameForm()
    return render(request, 'fmk/create_a_game.html', {'form': form})


def random_game(request):
    # A HTTP POST?
    context_dict = {}
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            game=form.save(commit=False)
            # For random games only scores of authorised users are stored.
            if request.user.is_authenticated():
                game.player = Player.objects.get(user=request.user)
                celeb1 = Celebrity.objects.get(celeb_id=request.POST.get("celeb_list1"))
                celeb2 = Celebrity.objects.get(celeb_id=request.POST.get("celeb_list2"))
                celeb3 = Celebrity.objects.get(celeb_id=request.POST.get("celeb_list3"))
                game.game_id = Game.objects.get_or_create(
                    creator=game.player,
                    celebrity1=celeb1,
                    celebrity2=celeb2,
                    celebrity3=celeb3,
                )[0]
                game.save()
                return index(request)
            else: return index(request)
        else:
            print form.errors
    else:
        form = ResultForm()
        celeb_list = Celebrity.objects.order_by('?')[:3]
        context_dict = {
            'random_celebs': celeb_list,
            'form': form
        }
    return render(request, 'fmk/random_game.html', context_dict)