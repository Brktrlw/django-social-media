

from django.urls import path
from .views import CreatePostView,DeletePostView
urlpatterns = [
    path("create/", CreatePostView.as_view(), name="url_createpost"),
    path("delete/<slug>",DeletePostView.as_view(),name="url_deletepost")
]
