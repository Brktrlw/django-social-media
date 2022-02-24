from django.contrib.auth.forms import UserCreationForm
from UserAPP.models import ModelUser
from django import forms
class FormUserCreate(UserCreationForm):
    first_name=forms.CharField(required=True)
    class Meta:
        model = ModelUser
        fields=(
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "profilePhoto"
        )

    def __init__(self, *args, **kwargs):
        super(FormUserCreate, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget=forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"İsim"})
        self.fields["last_name"].widget=forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Soy isim"})
        self.fields["username"].widget=forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Kullanıcı Adı"})
        self.fields["email"].widget=forms.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Email adresi"})
        self.fields["password1"].widget=forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Parola"})
        self.fields["password2"].widget=forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Parola Tekrarı"})
        self.fields["profilePhoto"].widget=forms.FileInput(attrs={"class":"form-control form-control-user","id":"uploadfile","style":"display:none"})

