

from django.urls import path
from .views import CreateLikePostView




urlpatterns = [
    path("likePost/<slug>",CreateLikePostView.as_view(),name="url_likepost")

]
