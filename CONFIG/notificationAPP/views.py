from django.shortcuts import redirect,HttpResponse
from django.views.generic import View
from notificationAPP.models import ModelNotification


class ReadAllNotifView(View):
    http_method_names = ["post"]

    def post(self,request):
        ModelNotification.objects.filter(receiverUser=request.user).update(isRead=True)
        return HttpResponse(status=201)
