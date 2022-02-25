from django.db import models
from UserAPP.models import ModelUser
from CommentAPP.models import ModelComment
from PostAPP.models import ModelPost
from django.db.models.signals import post_save
from django.dispatch import receiver


class ModelCommentLike(models.Model):
    user    = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı")
    comment = models.ForeignKey(ModelComment,on_delete=models.CASCADE,verbose_name="Yorum",related_name="likes")

class ModelPostLike(models.Model):
    user   = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Kullanıcı")
    post   = models.ForeignKey(ModelPost,on_delete=models.CASCADE,verbose_name="Gönderi",related_name="likes")

@receiver(post_save,sender=ModelPostLike)
def whenCreateUser(sender,instance,created,*args,**kwargs):
    LIKE_OBJ=ModelPostLike.objects.filter(user=instance.user,post=instance.post)
    if LIKE_OBJ.count()==2:
        LIKE_OBJ.delete()


