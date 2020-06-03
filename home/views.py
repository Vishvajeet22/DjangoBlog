from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, "about.html")
    
def blogs(request):
    return render(request, "blogs.html")
    
def contact(request):
    
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        feedback = request.POST['feedback']
        print(name, email, phone, feedback)

        if len(name)<2 or len(email)<4 or len(phone)<10 or len(feedback)<3:
            messages.error (request, "Please enter your details correctly")
        else:
            contact = Contact(name=name, email=email, phone= phone, feedback=feedback)
            contact.save()
            messages.success (request, "Thank you reaching out us. Good times!")

        contact = Contact(name=name, email=email, phone= phone, feedback=feedback)
        contact.save()

    return render(request, "contact.html")

def africa(request):
    return render(request, "africa.html")

def handleSignup(request):
    if request.method == 'POST':
        #get the post parameters
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        
        #checks
        if len(username) > 10:
            messages.error(request, "username must be less than 10 characters")
            return redirect("/")

        if not username.isalnum():
            messages.error(request, "username only contain letters and number")
            return redirect("/")

        #create a user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        myuser.save()
        messages.success(request, "Your Bloogers account has been succesfully created")
        return redirect("/")
    else:
        return HttpResponse("404 - Not Found")

def handleLogin(request):
    if request.method == 'POST':
        #get the post parameters
        loginusername = request.POST["loginusername"]
        loginpass = request.POST["loginpass"]
      
        user = authenticate(username = loginusername, password = loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been succesfully logged in")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/")

    return HttpResponse("404 - not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "You have been succesfully logged out")
    return redirect("/")

    
   

    