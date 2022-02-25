from django.shortcuts import HttpResponse,render
from django.views.generic import View
from notificationAPP.models import ModelNotification



class ListNotificationView(View):
    http_method_names = ["get"]
    def get(self,request):
        notifs=request.user.notifs.all().order_by("-createdDate")
        print(notifs)
        return render(request,"notifications.html",{"notifs":notifs})

class ReadAllNotifView(View):
    http_method_names = ["post"]

    def post(self,request):
        ModelNotification.objects.filter(receiverUser=request.user).update(isRead=True)
        return HttpResponse(status=201)
