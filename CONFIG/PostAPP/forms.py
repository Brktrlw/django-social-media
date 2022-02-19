from django import forms
from .models import ModelPost


class FormPost(forms.ModelForm):
    class Meta:
        model  = ModelPost
        fields = ("description","image")

    def __init__(self, *args, **kwargs):
        super(FormPost, self).__init__(*args, **kwargs)
        self.fields["description"].widget = forms.Textarea(
            attrs={"class": "form-control bg-light border-0 small", "placeholder": "İçerik","style":"margin-top: 1%; max-height: 150px; height: 204px;","maxlength":"500"})
        self.fields["image"].widget = forms.FileInput(
            attrs={"class": "custom-file-input","style":"margin-top: 1%;cursor: pointer;display:inline-block"})

