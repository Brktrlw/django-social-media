from django.db import models
from UserAPP.models import ModelUser
class ModelFollow(models.Model):
    follower  = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Takip Edilen",related_name="followers")
    following = models.ForeignKey(ModelUser,on_delete=models.CASCADE,verbose_name="Takip Eden",related_name="followings")

    class Meta:
        db_table            = "Follows"
        verbose_name        = "Takip"
        verbose_name_plural = "Takipçiler"

    def __str__(self):
        return f"Takip Eden {self.follower.username}-Takip Edilen {self.following.username}"