from django.shortcuts import render
from app1.models import product
# Create your views here.
def home(request):
    k=product.objects.all()
    return render(request,'home.html',{'k':k})
def login1(request):
    return render(request,'login.html')
def signup1(request):
    return render(request,'signup.html')
def prodetails(request,pk):
    k=product.objects.filter(id=pk)
    return render(request,'prodetails.html',{'k':k})
def cart(request):
    return render(request,'cart.html')