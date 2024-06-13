from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

#kayıt formu
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        
        #emaili zorunlu hale getirme
        self.fields['email'].required = True
        #isim soyisim zorunlu hale getirme
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    #email validation
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('bu email geçersiz')
        if len(email) >= 350:
            raise forms.ValidationError("bu email çok uzun")
        return email

#giriş formu    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput(), label='Şifre')

class UpdateUserForm(forms.ModelForm):
    password = None
    class Meta:
        model= User
        fields = ['first_name','last_name','username', 'email']
        exclude = ['password1', 'password1']
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        
        #emaili zorunlu hale getirme
        self.fields['email'].required = True
        #isim soyisim zorunlu hale getirme
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    #email validation
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('bu email kullanılıyor')
        if len(email) >= 350:
            raise forms.ValidationError("bu email çok uzun")
        return email    