from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from this_is_app.models import PredlojennieNovosti


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class PredlojenieNovostiForm(forms.ModelForm):
    class Meta:
        model = PredlojennieNovosti
        fields = [
            'post_category_from_user',
            'post_name_from_user',
            'post_descr_from_user',
            'post_photo_from_user',
        ]
        widgets = {
            'post_category_from_user': forms.Select(attrs={'class':'form_control'}),
            'post_name_from_user': forms.TextInput(attrs={'class':'form_control',
                                                       'placeholder':'Название'}),
            'post_descr_from_user': forms.Textarea(attrs={'class':'post_descr_from_user',
                                                        'placeholder':'Текст новости',
                                                        'rows':6}),
            'post_photo_from_user':forms.ClearableFileInput(attrs={'class':'form_control'})
        }