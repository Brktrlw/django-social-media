from django.views.generic import ListView

class ListFollowingsView(ListView):
    # takip ettiğimiz kullanıcılar
    template_name = "follows/follow.html"
    context_object_name = "users"
    paginate_by = 10

    def get_queryset(self):
        followings=self.request.user.followings.all().values_list("follower__username")
        return followings

class ListFollowersView(ListView):
    template_name = "follows/follower.html"
    context_object_name = "users"
    paginate_by = 10

    def get_queryset(self):
        followings = self.request.user.followers.all().values_list("following__username")
        return followings


