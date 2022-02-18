from django.shortcuts import render
from django.views import View

class LoginView(View):
    http_method_names = ["get","post"]
    def get(self,request):
        return render(request,"login.html")
    def post(self,reqeust):
        pass

class RegisterView(View):
    http_method_names = ["get","post"]
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        pass