from django.db import models
from django.utils.crypto import get_random_string
from UserAPP.models import ModelUser

def createNewUniqueID():
    return str(get_random_string(30))



class ModelComment(models.Model):
    user             = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı")
    text             = models.CharField(max_length=200,verbose_name="Yorum İçeriği")
    createdDate      = models.DateTimeField(auto_now_add=True)
    unique_id        = models.CharField(default=createNewUniqueID,editable=False,unique=True,max_length=30)


    class Meta:
        db_table = "Comments"
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"

    def __str__(self):
        return f"{self.user.username} - {self.text}"