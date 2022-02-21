from django.urls import path
from .views import ListFollowersView,ListFollowingsView
urlpatterns = [
    path("followers/",ListFollowersView.as_view(),name="url_followers"),
    path("followings/", ListFollowingsView.as_view(), name="url_followings"),
]
