from django.shortcuts import render
from django.views.generic import CreateView
from .forms import LikePostForm
from PostAPP.models import ModelPost

class CreateLikePostView(CreateView):
    http_method_names = ["post"]
    form_class = LikePostForm
    model = ModelPost

    def form_valid(self, form):
        print(form)

