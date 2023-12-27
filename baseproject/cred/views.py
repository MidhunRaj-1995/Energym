from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['email']
        password = request.POST['password']
        con_password= request.POST['con_password']
        if(password == con_password):
            if User.objects.filter(username=username).exists():
                messages.info(request,"The User name already taken")
                return redirect(demo)
            elif User.objects.filter(email=email).exists():
                messages.info(request, "The email already  taken")
                return redirect(demo)
            else:
                user =User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                messages.info(request, "done....")
        else:
            messages.info(request, "Password doesnot match...")
            return redirect(demo)
        return redirect(login_user)
    return render(request,"new_forms.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User = auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect(login_user)
    return render(request,"login_form.html")

def logout_user(request):
    auth.logout(request)
    return redirect("/")