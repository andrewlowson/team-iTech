from django.shortcuts import render
from django.http import HttpResponse
from fmk.models import Celebrity
from fmk.forms import SignUpForm, AddCategoryForm, AddCelebrityForm


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

def sign_up(request):
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(dats=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print user_form.errors
    else:
        user_form = SignUpForm()
    return render(request,
                  'fmk/sign_up.html',
                  {'user_form': user_form, 'registered': registered})



def add_category (request):
    #A HTTP POST?
    if request.method=='POST':
        form = AddCategoryForm(request.POST)

        #is the form valid?
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = AddCategoryForm()
    return render (request, 'fmk/add_category.html', {'form': form}
    )

def add_celebrity (request):
    #A HTTP POST?
    if request.method=='POST':
        form = AddCelebrityForm(request.POST)

        #is the form valid?
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = AddCelebrityForm()
    return render (request, 'fmk/add_celebrity.html', {'form': form}
    )