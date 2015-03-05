from django.shortcuts import render
from django.http import HttpResponse
from fmk.models import Celebrity


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
