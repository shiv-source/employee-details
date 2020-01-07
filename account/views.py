from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        email = request.POST['email']

        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password_1)
        user.save()
        print('user create')
        redirect('/')
    else:
        return render(request,'signup.html')