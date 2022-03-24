from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import random, string
# Create your views here.

def shorten(request):
    if request.method == "POST":
        l_url = request.POST.get("l_url")
        adress = str()
        for i in range(len(l_url)):
            if l_url[i] != '/' or l_url[i+1] == '/' or l_url[i-1] == '/':
                adress += l_url[i]
            else:
                break
        s_url =''.join(random.choice(string.ascii_letters) for x in range(8))
        s_url = adress + '/' + s_url
    else :
        s_url = ' '
    context = {
    "s_url" : s_url
    }
    return render(request, "urlapp/shorten.html",context)
    return s_url

