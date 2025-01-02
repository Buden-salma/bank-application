from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from bank.models import Balance_table
from bank.models import Transaction_history
from django.http import HttpResponse


def loginview(request):
    if request.user.is_authenticated:  # Fixed typo here
        return redirect('home') 
    if request.method=='POST':
        messages.info(request,'we are going to login you')
        a=request.POST.get('username')
        b=request.POST.get('password')
        obj1=authenticate(request,username=a,password=b)
        if obj1 is not None:
            login(request=request,user=obj1)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')
@login_required(login_url="login")
def homepage(request):
    obj2=User.objects.all()[::-1]
    return render(request,'home.html',{'res':obj2})
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def registerview(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        password = request.POST.get('passw')
        confirm_password = request.POST.get('cpass')
        email = request.POST.get('email')

        # Validate inputs
        if not all([username, first_name, last_name, password, confirm_password, email]):
            messages.error(request, "All fields are required.")
            return redirect('register')

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('register')

        if not password[0].isupper():
            messages.error(request, "Password must start with an uppercase letter.")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Create the user
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    return render(request, 'register.html')
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('firstname')
        c = request.POST.get('lastname')
        d = request.POST.get('passw')
        e = request.POST.get('cpass')
        f = request.POST.get('email')
        
        # Validate input
        if not all([a, b, c, d, e, f]):
            return render(request, 'register.html', {"error": "All fields are required."})
        
        if len(d) < 8:
            return render(request, 'register.html', {"error": "Password must be at least 8 characters long."})
        
        if not d[0].isupper():
            return render(request, 'register.html', {"error": "Password must start with an uppercase letter."})
        
        if e != d:
            return render(request, 'register.html', {"error": "Passwords do not match."})
        
        # Create the user object
        obj1 = User(username=a, first_name=b, last_name=c, email=f)
        obj1.set_password(d)
        obj1.save()
        
        return redirect('loginpage')

    # For GET requests or when validation fails
    return render(request, 'register.html')

@login_required(login_url='login')
def View_balance(request):
    obj1=Balance_table.objects.all()
    if request.user.is_superuser:
        if request.method=='POST':
            a=request.POST.get('Account_type')
            b=request.POST.get('Account_number',0)
            c=request.POST.get('balance',0)
            obj2=Balance_table(Account_type=a,Account_number=b,balance=c)
            obj2.save()
        return render(request,'viewbalance.html',{'all':obj1})
    return render(request,'viewbalance.html',{"all":obj1})
def historypage(request):
    obj3=Transaction_history.objects.filter(Customer_ID=request.user.id)
    return render(request,'history.html',{'res':obj3})
def Transfer(request):
    if request.method == 'POST':
        a=request.POST.get('Amount')
        b=request.POST.get('username')
        c=request.POST.get('payee_ID')
        new=User.objects.filter(username=b)[0] if User.objects.filter(username=b) else None

        obj4=Transaction_history(Amount=a,Customer_ID=new,payee_ID=c)
        obj4.save()
        return render(request,'transfer.html',{'res':obj4})
    
    return render(request,'transfer.html')
def logoutview(request):
    logout(request)
    return redirect('login')
from django.shortcuts import redirect
from django.contrib import messages
from .models import Balance_table

def deleteView(request, rid):
    if request.user.is_superuser:
        try:
            obj = Balance_table.objects.get(id=rid)
            obj.delete()
        except Balance_table.DoesNotExist:
            messages.error(request, "The record you are trying to delete does not exist.")
    else:
        messages.error(request, "nanu mosam cheyalevu, you are not admin")
    
    return redirect('home')


