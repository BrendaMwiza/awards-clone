from django import forms
from .models import Projects,Profile


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user_name', 'pub_date','rates','posting','views','profiles']
       
class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []