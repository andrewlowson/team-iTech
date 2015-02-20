from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("FMK...Let's do this!<br> <a href='/fmk/about/'>About</a>")


def about(request):
    return HttpResponse("FMK...is a fun game!<br><a href='/fmk/'>Index</a>")
