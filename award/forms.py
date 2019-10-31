from django import forms
from .models import Image,Profile,Rates

class Form(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user_name','profiles']

class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['follower', 'following']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ["design","usability","content"]