from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login

# passward for kunal is kunal#4545
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def home(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'home.html')
    
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
         login(request, user)
         return redirect("home")
        else:
         # No backend authenticated the credentials
         return render(request, 'login.html')
        
    
    return render(request, 'login.html')
    
def logoutuser(request):
    logout(request)
    return redirect('/')

def registeruser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')  # Redirect to the login page or wherever you want
        
    
    return render(request, 'register.html')