
from django.shortcuts import render
from .forms import RegisterForm

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
