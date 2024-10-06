#이미지 업로드 확인용
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'nickname', 'url']
