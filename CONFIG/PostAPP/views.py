from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from PostAPP.forms import FormPost
from PostAPP.models import ModelPost
from django.views.generic import DeleteView
from django.contrib import messages


class CreatePostView(View):
    # Post oluşturma sayfası
    http_method_names = ["post"]

    def post(self,request):
        form = FormPost(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            form.save_m2m()
        return redirect("url_homepage")

class DeletePostView(DeleteView):
    template_name = 'postshtml/silmeOnay.html'
    success_url = reverse_lazy("url_homepage")
    success_message = "Silme işlemi başarıyla gerçekleşti."

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("url_homepage")

    def get_queryset(self):
        post = ModelPost.objects.filter(user=self.request.user,slug=self.kwargs.get("slug"))
        return post

