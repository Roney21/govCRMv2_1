from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm


# Create your views here.

def index(request):
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
