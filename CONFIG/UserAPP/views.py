from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views import View
from .forms import FormUserCreate

class LoginView(View):
    """
    Giriş yaparken kullandığımız view
    """
    http_method_names = ["get","post"]
    def get(self,request):
        return render(request,"login.html")

    def post(self,reqeust):
        username=reqeust.POST.get("username")
        password=reqeust.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(reqeust, "Giriş bilgileriniz yanlış , lütfen tekrar deneyiniz.")
            return redirect("url_login")
        login(reqeust,user)
        messages.success(reqeust,f"Giriş işlemi başarılı. Hoş geldiniz {user.username}")
        return redirect("url_homepage")

class RegisterView(View):
    """
    Kayıt olurken kullandığımız view
    """
    http_method_names = ["get","post"]
    def get(self,request):
        form=FormUserCreate()
        return render(request,"register.html",{"form":form})
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        repassword=request.POST.get("repassword")
        surname= request.POST.get("surname")
        lastname= request.POST.get("lastname")
        profilePhoto=request.FILES.get("profilePhoto")

        return render(request,"register.html")