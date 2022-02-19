from django.views.generic import ListView
from FollowAPP.models import ModelFollow

class ListFollowingsView(ListView):
    # takip ettiğimiz kullanıcılar
    template_name = "follows/follow.html"
    context_object_name = "users"
    #paginate_by = 2

    def get_queryset(self):
        followings=self.request.user.followings.all().values_list("follower__username")
        print(followings)
        return followings

class ListFollowersView(ListView):
    template_name = "follows/follower.html"
    context_object_name = "users"
    # paginate_by = 2

    def get_queryset(self):
        followings = self.request.user.followers.all().values_list("following__username")
        return followings
