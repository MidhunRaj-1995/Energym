from django.http import HttpResponse
from django.shortcuts import render
from . models import place

def demo(request):
    obj = place.objects.all()
    return render(request,"admin_new.html",{"result":obj})

'''def login(request):
    return render(request,"forms_login.html")
def tables(request):
    return render(request,"tables.html")
def Thanks(request):
    return HttpResponse("Thank you for using our website.. visit again....")

def contact(request):
    return render(request,"contact.html")

def pass_val(request):
    name ="Midhun"
    place ="kerala"
    return render(request,"index.html",{"obj":name,"obj2":place})

def addition(request):
    x= int(request.GET["num1"])
    y= int(request.GET["num2"])
    return render(request,"index.html",{"obj1":x,"obj2":y,"obj3":(x+y),"obj4":(x-y),"obj5":(x*y),"obj6":})'''

