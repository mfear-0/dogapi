"""
Book: Building RESTful Python Web Services
"""
# Remember to import the appropriate class  
# Incase you receive an error here because of the Djnago version you have installed

# from django.urls import re_path -  Use this incase
from django.urls import re_path, include
from games import views


urlpatterns = [
    # You might also need to change url
    # in the following to re_path
    re_path(r'^breed/$', 
        views.BreedList.as_view(), 
        name=views.BreedList.name),
    re_path(r'^breed/(?P<pk>[0-9]+)/$', 
        views.BreedDetail.as_view(),
        name=views.BreedDetail.name),
    re_path(r'^dog/$', 
        views.DogList.as_view(),
        name=views.DogList.name),
    re_path(r'^dog/(?P<pk>[0-9]+)/$', 
        views.DogDetail.as_view(),
        name=views.DogDetail.name),
    # re_path(r'^players/$', 
    #     views.PlayerList.as_view(),
    #     name=views.PlayerList.name),
    # re_path(r'^players/(?P<pk>[0-9]+)/$', 
    #     views.PlayerDetail.as_view(),
    #     name=views.PlayerDetail.name),
    # re_path(r'^player-scores/$', 
    #     views.PlayerScoreList.as_view(),
    #     name=views.PlayerScoreList.name),
    # re_path(r'^player-scores/(?P<pk>[0-9]+)/$', 
    #     views.PlayerScoreDetail.as_view(),
    #     name=views.PlayerScoreDetail.name),
    re_path(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
