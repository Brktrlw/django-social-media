from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views import View
from .forms import FormUserCreate
from django.contrib.auth import logout
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
    form = FormUserCreate()

    def get(self,request):
        return render(request,"register.html",{"form":self.form})
    def post(self,request):
        form = FormUserCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect("url_homepage")
        else:
            for i in range(0,len(form.errors.values())):
                messages.error(request,list(form.errors.values())[i])
            return render(request,"register.html",{"form":self.form})

class LogoutView(View):
    http_method_names = ["get"]
    def get(self,request):
        logout(request)
        return redirect("url_homepage")

