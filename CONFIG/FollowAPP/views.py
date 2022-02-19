from django.views.generic import ListView
from FollowAPP.models import ModelFollow

class ListFollowingsView(ListView):
    # takip ettiğimiz kullanıcılar
    template_name = "follows/follow.html"
    context_object_name = "followingUser"
    #paginate_by = 2

    def get_queryset(self):
        followings=self.request.user.followings.all()
        print(followings)
        return followings

class ListFollowersView(ListView):
    pass
