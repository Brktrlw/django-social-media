

from django.urls import path
from .views import ViewHomePage,CreatePostView
urlpatterns = [
    path("",ViewHomePage.as_view(),name="url_homepage"),
    path("create-post/", CreatePostView.as_view(), name="url_createpost"),

]
