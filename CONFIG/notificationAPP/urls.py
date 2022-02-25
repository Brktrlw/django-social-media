

from django.urls import path
from .views import ReadAllNotifView

urlpatterns = [
    path("readallnotif/",ReadAllNotifView.as_view(),name="url_readallnotif")
]
