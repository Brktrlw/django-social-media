from django.contrib import admin
from .models import ModelUser
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    model        = ModelUser
    list_display = ("username","email")
    fieldsets    =  UserAdmin.fieldsets +(
        ("Profil Fotoğrafı Değiştirme",{
            "fields":["profilePhoto"]  # CustomUserModelimizdeki field alanının ismi
        }),
    )
admin.site.register(ModelUser,CustomAdmin)