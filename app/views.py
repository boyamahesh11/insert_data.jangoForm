from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        STD=StudentForm(request.POST)
        if STD.is_valid():
            sid=STD.cleaned_data['sid']
            sname=STD.cleaned_data['sname']
            semail=STD.cleaned_data['semail']
            print(sid)
            SO=Student.objects.get_or_create(sid=sid,sname=sname,semail=semail)[0]
            SO.save()

            d1={'SQS':Student.objects.all()}
            return render(request,'display_student.html',d1)
    return render(request,'insert_student.html',d)
