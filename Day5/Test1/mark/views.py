
from __future__ import unicode_literals
import re
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def details(request):
    student={"Name":[],"Class":[],"Mark":{"Maths":[],"Graphics":[],"OS":[]}}
    if request.POST :
        sname=request.POST['name']
        sclass=request.POST['class']
        sgraphics=request.POST['graphics']
        sos=request.POST['os']
        smaths=request.POST['maths']
        student["Name"].append(sname)
        student["Class"].append(sclass)
        student["Mark"]["Maths"].append(sgraphics)
        student["Mark"]["Graphics"].append(sos)
        student["Mark"]["OS"].append(smaths)
    return render(request,'hello.html',{"student":student})