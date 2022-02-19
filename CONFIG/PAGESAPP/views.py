from django.shortcuts import render
from django.views import View
from PostAPP.forms import FormPost
from PostAPP.models import ModelPost
from django.db.models import Q



class ViewHomePage(View):
    # Ana sayfada kullanıcının takip ettiği kullanıcıların gönderilerini listeler
    http_method_names = ["get"]
    def get(self,request):
        if request.user.is_authenticated:
            myFollowings = request.user.followings.all().values_list('follower_id')
            posts = ModelPost.objects.filter(Q(user_id__in=myFollowings) | Q(user=self.request.user)).order_by("-createdDate")

        form=FormPost()
        return render(request,"homepage.html",{"form":form,"posts":posts})


