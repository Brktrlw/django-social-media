

from django.urls import path
from .views import ViewHomePage
urlpatterns = [
    path("",ViewHomePage.as_view(),name="url_homepage")
]
