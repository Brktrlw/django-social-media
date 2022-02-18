from django import forms
from .models import ModelPost,ModelCategory
class FormPost(forms.ModelForm):
    class Meta:
        model  = ModelPost
        fields = ("title","description","categories","image")
    categories=forms.ModelMultipleChoiceField(queryset=ModelCategory.objects.all(),widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        super(FormPost, self).__init__(*args, **kwargs)
        self.fields["title"].widget = forms.TextInput(
            attrs={"class": "form-control bg-light border-0 small", "placeholder": "Başlık"})
        self.fields["description"].widget = forms.Textarea(
            attrs={"class": "form-control bg-light border-0 small", "placeholder": "İçerik","style":"margin-top: 1%; max-height: 150px; height: 204px;","maxlength":"500"})
        self.fields["image"].widget = forms.FileInput(
            attrs={"class": "custom-file-input","style":"margin-top: 1%;cursor: pointer;display:inline-block"})

