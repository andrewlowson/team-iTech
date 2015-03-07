from django.shortcuts import render
from django.http import HttpResponse
from fmk.models import Celebrity, Player
from fmk.forms import AddCategoryForm, AddCelebrityForm, CreateGameForm, UserForm


def index(request):
    most_f_list = Celebrity.objects.order_by('-fuck_count')[:5]
    most_m_list = Celebrity.objects.order_by('-marry_count')[:5]
    most_k_list = Celebrity.objects.order_by('-kill_count')[:5]
    context_dict = {
        'boldmessage': "FMK will be awesome...eventually.",
        'fuck_list': most_f_list,
        'marry_list': most_m_list,
        'kill_list': most_k_list,
    }

    return render(request, 'fmk/index.html', context_dict)


def about(request):

    return render(request, 'fmk/about.html')


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
        form.creator = request.user
        # is the form valid?
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CreateGameForm()
    return render(request, 'fmk/create_a_game.html', {'form': form})


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            Player.objects.get_or_create(user = user)[0]

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'fmk/register.html',
            {'user_form': user_form, 'registered': registered} )