
from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import render, redirect
from .forms import AadharForm,StudentForm
from .models import Aadhar



def home(request):
    if request.method == "POST":
        print("heloooo")
        form = RegisterForm(request.POST)
        # print(form)
        if form.is_valid(): 
            form.save()
            return render(request, "success.html")
    else:
        form = RegisterForm()

    return render(request, "home.html", {"form": form})


def aadhar(request):
    if request.method == "POST":
        form = AadharForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')

    else:
        form = AadharForm()

    return render(request, "aadhar.html", {"form": form,"aadhar":True})


def student(request):
    success = False
    all_adhars = Aadhar.objects.all()  

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = StudentForm()

    return render(request, "student.html", {"form": form,"success": success, "all_adhars": all_adhars  
    })



