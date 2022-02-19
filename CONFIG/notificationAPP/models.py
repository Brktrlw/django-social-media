from django.db import models
from UserAPP.models import ModelUser

class ModelNotification(models.Model):
    NOTIFICATION_TYPE = (
        ("1", "Takip"),
        ("2", "Yorum"),
        ("3", "Beğeni"),
    )
    receiverUser = models.ForeignKey(ModelUser,on_delete=models.CASCADE,related_name="notifs",verbose_name="Alan Kullanıcı")
    content      = models.CharField(max_length=250,verbose_name="Bildirim İçeriği")
    isRead       = models.BooleanField(default=False,verbose_name="Okundu mu")
    senderUser   = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Gönderen Kullanıcı")
    createdDate  = models.DateTimeField(auto_now_add=True)
    kind         = models.CharField(choices=NOTIFICATION_TYPE,max_length=7)