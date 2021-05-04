from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"] 
       
class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Username")
    password = forms.CharField(max_length=20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm Password",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords don't match")

        values = {
            "username" : username,
            "password" : password
        }
        return values



class interests_form(forms.ModelForm):
    interests = forms.CharField(label="")
    class Meta:
        model = Profile
        fields = ["interests"]

class youtube_form(forms.ModelForm):
    youtube_id = forms.CharField(label ="")
    class Meta:
        model = Profile
        fields = ['youtube_id']  

class instagram_form(forms.ModelForm):
    instagram_id = forms.CharField(label = "")
    class Meta:
        model = Profile
        fields = ['instagram_id']   
    
class twitter_form(forms.ModelForm):    
    twitter_id = forms.CharField(label = "")
    class Meta:
        model = Profile
        fields = ['twitter_id'] 

class facebook_form(forms.ModelForm):
    facebook_id = forms.CharField(label = "")
    class Meta:
        model = Profile
        fields = ['facebook_id']

class spotify_form(forms.ModelForm):
    spotify_id = forms.CharField(label = "")
    class Meta:
        model = Profile
        fields = ['spotify_id'] 

class soundcloud_form(forms.ModelForm):
    soundcloud_id = forms.CharField(label = "")
    class Meta:
        model = Profile
        fields = ['soundcloud_id'] 

class phone_form(forms.ModelForm):
    phone = forms.CharField(label = "")
    class Meta:
        model = Profile
        fields = ['phone'] 

class email_form(forms.ModelForm):
    email = forms.CharField(label = "")
    class Meta:
        model = Profile
        fields = ['email'] 