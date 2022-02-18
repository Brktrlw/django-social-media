

from django.urls import path
from .views import LoginView,RegisterView,LogoutView
urlpatterns = [
    path("login/",LoginView.as_view(),name="url_login"),
    path("register/",RegisterView.as_view(),name="url_register"),
    path("logout/", LogoutView.as_view(), name="url_logout"),
]

