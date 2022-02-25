

def navbar_data(request):
    context = dict()
    if request.user.is_authenticated:
        context["notifications"] = request.user.notifs.all()
    return context