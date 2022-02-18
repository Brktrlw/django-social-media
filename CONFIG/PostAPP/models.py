from django.db import models
from UserAPP.models import ModelUser
from autoslug import AutoSlugField

class ModelPost(models.Model):
    user        = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı",related_name="posts")
    title       = models.CharField(max_length=200,verbose_name="Başlık")
    image       = models.ImageField(upload_to="PostImages",null=False,blank=False)
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    slug        = AutoSlugField(populate_from="title",unique=True)

    class Meta:
        db_table            = "Posts"
        verbose_name        = "Gönderi"
        verbose_name_plural = "Gönderiler"

    def __str__(self):
        return self.title
