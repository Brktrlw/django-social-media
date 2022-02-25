from django.db import models
from UserAPP.models import ModelUser
from CommentAPP.models import ModelComment
from PostAPP.models import ModelPost
from django.db.models.signals import post_save
from django.dispatch import receiver
from notificationAPP.models import ModelNotification
from crum import get_current_request


class ModelCommentLike(models.Model):
    user    = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı")
    comment = models.ForeignKey(ModelComment,on_delete=models.CASCADE,verbose_name="Yorum",related_name="likes")

class ModelPostLike(models.Model):
    user   = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı")
    post   = models.ForeignKey(ModelPost,on_delete=models.CASCADE,verbose_name="Gönderi",related_name="likes")

@receiver(post_save,sender=ModelPostLike)
def whenCreateUser(sender,instance,created,*args,**kwargs):
    loggedUser=get_current_request().user
    # Giriş yapmış kullanıcı daha önce beğenip beğenmediğini kontrol ediyoruz
    LIKE_OBJ=ModelPostLike.objects.filter(user=loggedUser,post=instance.post)
    if LIKE_OBJ.count()==2:
        #eğer beğenmişse
        LIKE_OBJ.delete()
        ModelNotification.objects.filter(receiverUser=instance.post.user,kind="3",post=instance.post,senderUser=loggedUser).delete()
    else:
        #eğer beğenmemişse
        if instance.post.user !=loggedUser:
            notificationText=f"{loggedUser.username} senin gönderini beğendi."
            ModelNotification.objects.create(
                receiverUser=instance.post.user,
                kind="3",post=instance.post,
                senderUser=loggedUser,
                content=notificationText
            )


