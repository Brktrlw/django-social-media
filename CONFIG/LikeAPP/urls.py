

from django.urls import path
from .views import CreatePostLikeView




urlpatterns = [
    path("postlike/", CreatePostLikeView.as_view(), name="url_postlike"),
]
