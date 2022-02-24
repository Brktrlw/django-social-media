from django import forms
from .models import ModelPostLike,ModelCommentLike

class LikePostForm(forms.ModelForm):
    class Meta:
        model=ModelPostLike
        fields=("post",)