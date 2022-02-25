

from django.urls import path
from .views import ReadAllNotifView,ListNotificationView

urlpatterns = [
    path("readallnotif/",ReadAllNotifView.as_view(),name="url_readallnotif"),
    path("bildirimler/",ListNotificationView.as_view(),name="url_listnotification")
]
