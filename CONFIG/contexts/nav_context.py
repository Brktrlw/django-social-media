

def navbar_data(request):
    context = dict()
    if request.user.is_authenticated:
        context["notifications"] = request.user.notifs.all().order_by("-createdDate")[:7]
        context["notifCount"] =request.user.notifs.filter(isRead=False).count()
    return context