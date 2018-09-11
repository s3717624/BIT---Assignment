from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

def home(request):
    return render(request, "home.html")

def user(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            userin = form.cleaned_data['username']
            print(userin)
            return render(request, "user.html", {'userin': userin})
        else:
            return render(request, "home.html")

        #username = request.POST.get('textfield', None)

def main(request):
    return render(request, "main.html")

