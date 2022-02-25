from django.views.generic import CreateView
from LikeAPP.models import ModelPostLike
from PostAPP.models import ModelPost
from django.shortcuts import redirect


class CreateLikePostView(CreateView):
    template_name = "homepage.html"
    http_method_names = ["post"]
    model = ModelPostLike
    queryset = ModelPostLike.objects.all()

    def post(self, request, *args, **kwargs):
        post=ModelPost.objects.get(slug=self.kwargs.get("slug"))
        ModelPostLike.objects.create(user=request.user,post=post)
        return redirect("url_homepage")