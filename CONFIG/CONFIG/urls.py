
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("PAGESAPP.urls")),
    path("user/",include("UserAPP.urls")),
    path("post/",include("PostAPP.urls")),
    path("follows/",include("FollowAPP.urls"))
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
