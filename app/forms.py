
from django import forms
from .models import Registration
from .models import Aadhar
from .models import Student



# class Regform(forms.form):
#     Name = forms.CharField()
#     Email = forms.EmailField()
#     Contact = forms.IntegerField()



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class AadharForm(forms.ModelForm):
    class Meta:
        model = Aadhar
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_adhar_no(self):
        adhar = self.cleaned_data.get('adhar_no')
        if Student.objects.filter(adhar_no=adhar).exists():
            raise forms.ValidationError("This Aadhaar number already exists.")
        return adhar