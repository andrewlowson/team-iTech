from django.conf.urls import patterns, url
from fmk import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^add_category/$', views.add_category, name= 'add_category'),
    url(r'^add_celebrity/$', views.add_celebrity, name= 'add_celebrity'),
    url(r'^top_tables/$', views.top_tables, name= 'top_tables'),
    url(r'^play/$', views.play, name= 'play'),
    url(r'^play/create_game/$', views.create_game, name= 'create_game'),
    url(r'^play/random_game/$', views.random_game, name= 'random_game'), 
)

