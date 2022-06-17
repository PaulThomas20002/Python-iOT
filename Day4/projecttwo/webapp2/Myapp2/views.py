# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from distutils.util import execute

from django.shortcuts import render
import MySQLdb 
con=MySQLdb.connect("localhost","root","","dbname")
c=con.cursor()
# Create your views here.
#def main(request):
 #   return render(request,'index.html')
def registration(request):
    if request.POST:
        nme=request.POST["t1"]
        age=request.POST["t2"]
        dob=request.POST["t3"]
        mail=request.POST["t4"]
        phone=request.POST["t5"]
        c.execute("INSERT INTO registration VALUES(%s,%s,%s,%s,%s)",[Name,Age,DOB,Mail,Phone])
        con.commit()
    return render(request,"index.html")
