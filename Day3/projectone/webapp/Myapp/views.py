# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render


# Create your views here.
def add(request):
    c=0
    if request.POST:
        a=int(request.POST["t1"])
        b=int(request.POST["t2"])
        c=a+b
        print(a,"+",b,"=",c)       
    return render(request,"index.html",{"result":c})
def subtract(request1):
    c=0
    if request1.POST:
        a=int(request1.POST["t4"])
        b=int(request1.POST["t5"])
        c=a-b
        print(a,"-",b,"=",c)
    return render(request1,"sub.html",{"result":c})
def main(request2):
    c=0
    if request2.POST:
        a=int(request2.POST["t1"])
        b=int(request2.POST["t2"])
        if "b1" in request2.POST:
            c=a+b
        if "b2" in request2.POST:
            c=a-b
        if "b3" in request2.POST:
            c=a*b
        if "b4" in request2.POST:
            c=a/b
    return render(request2,"main.html",{"result":c})

    