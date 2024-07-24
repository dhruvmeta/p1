from django.shortcuts import render
from .forms import userdetialsform

# Create your views here.

def index (request):
    if request.method=='POST':
        user=userdetialsform(request.POST)
        if user.is_valid():
            user.save()
            print("date hase been upload")
        else:
            print(user.errors)
    return render (request,'index.html')

def about (request):
    return render (request,'about.html')

def contact (request):
    return render (request,'contact.html')

def project (request):
    return render (request,'project.html')

def testimonial (request):
    return render (request,'testimonial.html')
