
from django import forms
from .models import Registration

# class Regform(forms.form):
#     Name = forms.CharField()
#     Email = forms.EmailField()
#     Contact = forms.IntegerField()



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'