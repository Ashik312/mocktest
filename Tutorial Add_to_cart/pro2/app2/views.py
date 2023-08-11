from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from app2.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from cart.cart import Cart

# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{"products":products})

def productview(request,pk):
    k=Product.objects.filter(id=pk)
    return render(request,'productview.html',{"k":k})
def signup_user(request):
    if request.user.is_authenticated:
        return home(request)
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confpassword')
            if password==confirm_password:
                if User.objects.filter(username=name,email=email).exists():
                    messages.info(request,"username Already Exists")
                    print('Already Have')
                else:
                    new=User.objects.create_user(username=name,password=password,email=email)
                    new.set_password(password)
                    new.save()
                    return redirect(login_user)
            else:
                print('wrong password')
    return render(request,'signup.html')  
def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            HttpResponse("Inavalid")
    return render(request,'login_user.html')
def logoutuser(request):
     logout(request)
     return redirect(login_user)



@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')