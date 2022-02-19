from django.db import models
from UserAPP.models import ModelUser
from django.utils.crypto import get_random_string

def create_new_ref_number():
    return str(get_random_string(30))



class ModelPost(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",related_name="posts")
    description = models.TextField(max_length=500,verbose_name="İçerik",null=True,blank=True)
    image       = models.ImageField(upload_to="PostImages",null=True,blank=True)
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    slug        = models.CharField(max_length=30,default=create_new_ref_number,editable=False, unique=True)

    class Meta:
        db_table            = "Posts"
        verbose_name        = "Gönderi"
        verbose_name_plural = "Gönderiler"

    def getLikeCount(self):
        pass
    def getCommentCount(self):
        pass

