from django.shortcuts import render,redirect
from django.views import View
from PostAPP.forms import FormPost
from django.views.generic.edit import CreateView
from PostAPP.models import ModelPost

class CreatePostView(View):
    http_method_names = ["post"]

    def post(self,request):
        form = FormPost(request.POST,request.FILES)
        print(form)

        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            form.save_m2m()
        return redirect("url_homepage")

class ViewHomePage(View):
    http_method_names = ["get"]
    def get(self,request):
        if request.user.is_authenticated:
            posts=ModelPost.objects.all().order_by("-createdDate")
        form=FormPost()
        return render(request,"homepage.html",{"form":form,"posts":posts})


