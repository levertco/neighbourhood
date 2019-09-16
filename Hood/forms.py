
from django import forms
from .models import User_profile,Post


class EditProfile(forms.ModelForm):
    
    class Meta:
        model = User_profile
        fields = ['name', 'email']
    

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ['user','profile']