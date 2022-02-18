from django.contrib import admin
from .models import ModelUser
from django.contrib.auth.admin import UserAdmin
from PostAPP.models import ModelPost
from CommentAPP.models import ModelComment

class CustomAdmin(UserAdmin):
    model        = ModelUser
    list_display = ("username","email")
    fieldsets    =  UserAdmin.fieldsets +(
        ("Profil Fotoğrafı Değiştirme",{
            "fields":["profilePhoto"]  # CustomUserModelimizdeki field alanının ismi
        }),
    )
admin.site.register(ModelUser,CustomAdmin)
admin.site.register(ModelPost)
admin.site.register(ModelComment)



