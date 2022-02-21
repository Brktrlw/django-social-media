from django.db import models
from django.contrib.auth.models import AbstractUser



class ModelUser(AbstractUser):
    profilePhoto = models.ImageField(upload_to="ProfilePhotos", blank=True, null=True)
    biography    = models.CharField(verbose_name="Biyogrofi",blank=True,null=True,max_length=150,default="ProfilePhotos/default.webp")

    class Meta:
        db_table            = "Users"
        verbose_name        = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"

    def __str__(self):
        return self.username
