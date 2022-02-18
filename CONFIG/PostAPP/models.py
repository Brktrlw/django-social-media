from django.db import models
from UserAPP.models import ModelUser


class ModelPost(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",related_name="posts")
    title       = models.CharField(max_length=200,verbose_name="Başlık")
    image       = models.ImageField(upload_to="PostImages",null=False,blank=False)
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
