from django.db import models
from django.db import models
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator,
                                    RegexValidator,
                                    EmailValidator,
                                    MinLengthValidator,
                                    MaxLengthValidator,
                                    )
from django.core.exceptions import ValidationError
from django import forms


# Create your models here.

# --- Custom Validators ---
def validate_name(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError("Name must contain alphabets only.")


def validate_mobile(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("Mobile number must be exactly 10 digits.")


def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in value):
        raise ValidationError("Password must include at least one number.")
    if not any(char.isalpha() for char in value):
        raise ValidationError("Password must include at least one alphabet.")
    if not any(char in "@#$%^&*!" for char in value):
        raise ValidationError("Password must contain a special character (@#$%^&*! )")


# --- Registration Model ---

class Registration(models.Model):
    username = models.CharField(max_length=30,unique=True,validators=[validate_name],)
    name = models.CharField(max_length=50,validators=[validate_name],)
    email = models.EmailField(unique=True,validators=[EmailValidator()])
    mobile = models.CharField(max_length=10,validators=[validate_mobile],unique=True)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    address = models.TextField()
    password = models.CharField(max_length=50,validators=[validate_password])
    confirm_password = models.CharField(max_length=50)


    # Model-level validation for confirm password
    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError("Password and Confirm Password must match.")
        
    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.username
    
class Aadhar(models.Model):
    adhar_no=models.IntegerField(unique=True)
    create_at=models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
       return str(self.adhar_no)

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    adhar_no=models.OneToOneField(Aadhar,on_delete=models.PROTECT)


    