from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Site_user



def loginpage(request):
    if request.method == "POST":
          username=request.POST.get('username')
          password=request.POST.get('password')

          if not User.objects.filter(username=username).exists():
              
                messages.error(request,"Invalid Username!")
                return redirect("login")
          
          user=authenticate(username=username,password=password)

          if user is None:
            messages.error(request,"Invalid Password")
            return redirect("login")
          
          else:
               login(request,user)
               return redirect("index")

    return render(request, 'login.html')

#signup-------------------------------

def registeruser(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')

  
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('registeruser')

        
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)  
        user.save()  

        site_user = Site_user.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_no,
            email=email,
            address=address,
        )

        messages.success(request, 'Account created successfully!')

        return redirect('login') 

    return render(request, 'registeruser.html')



#logout----------------------

def logout_page(request):
    logout(request)
    return redirect('login')
