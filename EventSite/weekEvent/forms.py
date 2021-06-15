from django import forms
from django.forms import ClearableFileInput
from .models import Image,Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets={
            'image': ClearableFileInput(attrs={'multiple':True},)
        }
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class UserRegisterationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username','email',)