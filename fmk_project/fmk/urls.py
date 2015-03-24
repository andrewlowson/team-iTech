from django.conf.urls import patterns, url
from fmk import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^add_category/$', views.add_category, name= 'add_category'),
    url(r'^add_celebrity/$', views.add_celebrity, name= 'add_celebrity'),
    url(r'^create_a_game/$', views.add_game, name='add_game'),
    url(r'^top_tables/$', views.top_tables, name= 'top_tables'),
    url(r'^play/random_game/$', views.random_game, name= 'random_game'),
    url(r'^play/(?P<gameID>[\w\-]+)/$', views.playgame, name='play_game'),
    url(r'^site_map/$', views.site_map, name='site_map'),
)

