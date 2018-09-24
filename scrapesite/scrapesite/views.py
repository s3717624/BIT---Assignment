from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm
from .WebScraping import *
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

            time, info, color = scrapefunction(userin, passin)

            data = zip(time, info)
            colorsorted = []
            palette = ['255, 128, 128', '255, 179, 179', '179, 89, 89', '128, 255, 128', '179, 255, 179', '89, 179, 89', '128, 128, 255', '179, 179, 255', '89, 89, 179', '255, 128, 255', '255, 179, 255', '179, 89, 179', '255, 210, 128', '255, 228, 179', '179, 147, 89']

            def sortbylength(s):
                return s[0][3:8]

            data = sorted(data, key=sortbylength)

            j = 0
            for c in color:
                if color[j] == 'newcourse':
                    del color[j+1]
                j +=1

            j = 0
            color.append('end')
            color.append('end')
            color.append('end')
            while j < len(color):
                if color[j] == 'end':
                    break
                if color[j] == 'newcourse':
                    colorsorted.append(color[j+1])
                    if color[j+2] == 'newcourse':
                        colorsorted.append('none')
                        colorsorted.append('none')
                    else:
                        colorsorted.append(color[j+2])
                        if color[j+3] == 'newcourse':
                            colorsorted.append('none')
                        else:
                            colorsorted.append(color[j+3])
                j += 1

            bg = {k: v for k, v in zip(colorsorted, palette)}
            colorcode = []
            code = []
            for cp in list(bg):
                if cp != 'none' and cp != 'end':
                    colorcode.append('<div class="colorcode"><div class="color" style="background-color: rgba(' + bg[cp] + ');"></div>' + '<span class="colortext">' + cp[:-3] + ' ' + cp[-3:] + '</span>' + '</div>')
                    code.append('<div class="code" style="display: none;">' + bg[cp] + '</div>')

            xdict = {'Mon': 97, 'Tue': 300, 'Wed': 503, 'Thu': 706, 'Fri': 909}
            ydict = {'06:00': 36, '06:30': 71, '07:00': 106, '07:30': 141, '08:00': 176, '08:30': 211, '09:00': 246, '09:30': 281, '10:00': 316, '10:30': 351, '11:00': 386, '11:30': 421, '12:00': 456, '12:30': 491, '13:00': 526, '13:30': 561, '14:00': 596, '14:30': 631, '15:00': 666, '15:30': 701, '16:00': 736, '16:30': 771, '17:00': 806, '17:30': 841, '18:00': 876, '18:30': 911, '19:00': 946, '19:30': 981, '20:00': 1016, '20:30': 1051, '21:00': 1086, '21:30': 1121}
            xshift = {}
            divs = []
            height = 59
            gradient = 0.7
            name = 0

            for t, i in data:

                if '2 hrs' in t:
                    height = 129
                    gradient = 0.5
                else:
                    height = 59
                    gradient = 0.7

                if t[0:8] not in xshift:
                    xshift[t[0:8]] = 0

                divs.append('<div onclick="raise(this)" class="cell" style="left: ' + str(xdict[t[0:3]]+xshift[t[0:8]]) + 'px; top: ' + str(ydict[t[3:8]]) + 'px; ' + 'height: ' + str(height) + 'px; ' + 'background: linear-gradient(0deg, rgba(' + bg[i[0]+i[1]] + ',' + str(gradient) + ') 0%, rgba(' + bg[i[0]+i[1]] + ',' + '1) 50%);' + '">' + '<div class="celltext">' + i[0] + '<br>' + i[1] + '<br>' + i[2] + '</div>' + '</div>')
                xshift[t[0:8]] = xshift[t[0:8]]+26

            return render(request, 'user.html', {'divs': divs, 'colorcode': colorcode, 'code': code})

        else:
            return render(request, "home.html")

def main(request):
    return render(request, "main.html")