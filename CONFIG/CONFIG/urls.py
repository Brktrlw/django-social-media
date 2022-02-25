
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404




urlpatterns = [
    path('admin/', admin.site.urls,),
    path("",include("PAGESAPP.urls"),),
    path("user/",include("UserAPP.urls")),
    path("post/",include("PostAPP.urls")),
    path("follows/",include("FollowAPP.urls")),
    path("like/",include("LikeAPP.urls")),
    path("notification/",include("notificationAPP.urls"))
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handler404 = 'PAGESAPP.views.page404'