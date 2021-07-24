from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile,CompanyProfile
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email','firstname','lastname','phone_number')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','firstname','lastname','phone_number')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)

class CompanyProfileForm(forms.ModelForm):
    
    class Meta:
        model = CompanyProfile
        fields = "__all__"
        exclude = ('owner',)

