from django.contrib import messages
from django.contrib.auth import login
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm, RegisterForm


# Create your views here.

def index(request):
    regform = RegisterForm()  # Реестрація користувача
    if request.method == "POST":
        regform = RegisterForm(request.POST)
        if regform.is_valid():
            user = regform.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, 'homepage/index.html', {
        'regform': regform
    })
    regform = RegisterForm()

    if request.method == "POST" and request.FILES["file"]:
        form = UserForm
        myfile = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'homepage/index.html', {
            'form': form
        })

    return render(request, 'homepage/index.html')


def handle_uploaded_file(f):
    with open('/aaaaaaaaaaaaaaaa/', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

