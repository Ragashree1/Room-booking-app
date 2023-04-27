from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        user = authenticate(request, username=username, password=password)
        if user is None or user.user_type != user_type:
            messages.error(request, 'invalid username or password')
            return render(request, 'registration/login.html')
        else:
            if user.user_type == 'S':
                return student(request)
            elif user.user_type == 'T':
                return render(request,'registration/staff.html')
    else:
        return render(request, 'registration/login.html')
        
            

def student(request):
    return render(request, 'registration/student.html')
def home(request):
    return render(request, 'registration/home.html')

