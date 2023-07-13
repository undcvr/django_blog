from django import forms
from .models import Post
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'profile_pic']
      
# class SignUpUserForm(UserCreationForm):
#     username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form_input'})),
#     password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form_input'})),
#     password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class': 'form_input'})),
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form_input'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form_input'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form_input'}),
#         }
