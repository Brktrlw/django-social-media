from django.contrib import admin
from .models import ModelUser
from django.contrib.auth.admin import UserAdmin
from PostAPP.models import ModelPost
from CommentAPP.models import ModelComment
from FollowAPP.models import ModelFollow
from LikeAPP.models import ModelCommentLike,ModelPostLike
from notificationAPP.models import ModelNotification
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
admin.site.register(ModelCommentLike)
admin.site.register(ModelPostLike)
admin.site.register(ModelFollow)
admin.site.register(ModelNotification)

