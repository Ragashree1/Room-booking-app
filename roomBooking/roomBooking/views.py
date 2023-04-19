from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        user = authenticate(request, username=username, password=password)
        if user is None or user.user_type != user_type:
            return render(request, 'registration/login.html')
        else:
            if user.user_type == 'S':
                return render(request,'registration/student.html')
            elif user.user_type == 'T':
                return render(request,'registration/staff.html')


def home(request):
    return render(request, 'registration/home.html')

