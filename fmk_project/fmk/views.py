from django.shortcuts import render

from django.http import HttpResponse


def index(request):

	context_dict = {'boldmessage': "FMK will be awesome...eventually."}
        return render(request, 'fmk/index.html',context_dict)

def about(request):

    return render(request, 'fmk/about.html')
