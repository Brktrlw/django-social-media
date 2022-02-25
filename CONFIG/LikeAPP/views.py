from django.views.generic import CreateView
from LikeAPP.models import ModelPostLike
from PostAPP.models import ModelPost
from django.shortcuts import redirect,HttpResponse
import json

class CreatePostLikeView(CreateView):
    http_method_names = ["post"]
    model = ModelPostLike
    queryset = ModelPostLike.objects.all()
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        post=ModelPost.objects.get(slug=data.get("slug"))
        ModelPostLike.objects.create(user=request.user,post=post)
        return HttpResponse(status=201)