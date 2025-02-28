from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
  return render(request, 'mobilia/home.html')

def Shop(request):
  return render(request, 'mobilia/shop.html' )

def About(request):
  return render(request, 'mobilia/about.html' )

def Service(request):
  return render(request, 'mobilia/services.html' )

def Blog(request):
  return render(request, 'mobilia/blog.html' )

def Contact(request):
  return render(request, 'mobilia/contact.html' )

def Cart(request):
  return render(request, 'mobilia/cart.html' )


def Checkout(request):
  return render(request, 'mobilia/checkout.html' )

def ConfromOrder(request):
  return render(request, 'mobilia/thankyou.html' )



def profile(request):
    return render(request, 'Login/profile.html', context={})



def sign_up(request):
    registered =False
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            return HttpResponse("Password not same")
        data = User.objects.create_user(username,email,pass1)
        data.save()
        registered = True
            
    dict = {'registered': registered}
    return render(request, 'Login/signup.html', context=dict)


def Login(request):
    Login = False
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
           Login = True
    dict = {'Login': Login}
    return render(request, 'Login/login.html', context=dict)

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    return render(request, 'Login/profile.html', context={})