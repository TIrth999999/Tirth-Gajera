from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth.models import User,AnonymousUser
# from django.contrib.auth import authenticate,login,logout
from app.models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email,subject=subject,message=message)
        contact.save()

        def __str__(self):
            return self.name
                
    return render(request,'index.html')