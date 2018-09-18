from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .WebScraping import scrapefunction

import sys

from subprocess import run, PIPE


def home(request):
    return render(request, "home.html")

def user(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            userin = form.cleaned_data["username"]
            passin = form.cleaned_data["password"]

            scrapefunction(userin, passin)


            #p = run(["WebScraping.py", userin, password], stdout=PIPE, input=None, encoding='utf-8')
            #p = run(["/home/skvutte/PycharmProjects/WebScrape/scrapesite/WebScraping.py"], stdout=PIPE, input=None, encoding='utf-8')

            #if p.returncode != 0: raise Exception

            #print(p.stdout)
            #return p.stdout

        else:
            return render(request, "home.html")

        #username = request.POST.get('textfield', None)

def main(request):
    return render(request, "main.html")

