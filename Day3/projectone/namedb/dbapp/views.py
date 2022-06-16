# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def main(request):
    stud={}
    if request.POST:
        nme=request.POST["t1"]
        clas=request.POST["t2"]
        mrk1=request.POST["t3"]
        mrk2=request.POST["t4"]
        mrk3=request.POST["t5"]

        stud={"name":nme,"class":clas,"mark1":mrk1,"mark2":mrk2,"mark3":mrk3}
        #stud={"name":nme,"class":clas}
    return render(request,"index.html",{"result":stud})