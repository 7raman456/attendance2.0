from django.shortcuts import render
from stubase.models import students
from stubase.models import attendance as a
from django.http import HttpResponse
from datetime import date
import datetime
from stubase import variables
from django.shortcuts import redirect
# Create your views here.
def front(request):
   return render(request,"front.html",{"classes":variables.classes})

def master(request):
   return render(request,"master.html",{"classes":variables.classes})

def addstu(request,classs):
   if(request.method=='POST'):
      print(request.POST.get)
      stu=students( name=request.POST.get('name') , classandsec=classs)
      stu.save()
      return redirect(addstu,classs)
   return render(request,'addstudent.html',{"classes":variables.classes})


def attendance(request,classs):
   studentlist=students.objects.all().filter(classandsec=classs).order_by('name')
   if(request.method=='POST'):
      print(request.POST.get)
      today = date.today()
      d1 = today.strftime("%Y-%m-%d")
      entry=a(name=request.POST.get('name'),date=d1,classandsec=classs)
      entry.save()
      return HttpResponse("done"+str(datetime.datetime.now()))
   return render(request,'attendance.html',{'studentlist':studentlist})

def removestu(request,classs):
   studentlist=students.objects.all().filter(classandsec=classs).order_by('name')
   if(request.method=='POST'):
      print(request.POST.get)
      r=students.objects.get(name=request.POST.get('name') , classandsec=classs)
      print(r)
      r.delete()
      return HttpResponse("removed"+str(datetime.datetime.now()))
   return render(request,'removestu.html',{'studentlist':studentlist})

def attendents(request,classs):
   studentlist=students.objects.all().filter(classandsec=classs).values_list('name',flat=True)
   studentlist = list(studentlist)
   today = date.today()
   d1 = today.strftime("%Y-%m-%d")
   presentlist=a.objects.all().filter(date=d1,classandsec=classs).values_list('name',flat=True)
   presentlist=list(presentlist)
   absentlist=set(studentlist) - set(presentlist)
   # print(absentlist);
   return render(request,'attendents.html',{'studentlist':studentlist ,'presentlist':presentlist,'absentlist':absentlist })


def run(request):
   names="hdhaj,ai  db,iyadh,aied"
   name=names.split(',')

   for x in name:
      print(x);
      # stu = students(name=request.POST.get('name'), classandsec=classs)
      # stu.save()



   return HttpResponse("done")