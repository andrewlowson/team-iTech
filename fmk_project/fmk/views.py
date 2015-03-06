from django.shortcuts import render
from django.http import HttpResponse
from fmk.models import Celebrity
from fmk.forms import AddCategoryForm, AddCelebrityForm


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