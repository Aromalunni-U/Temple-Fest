from django.shortcuts import render, get_object_or_404,redirect
from .models import Service,Comment,Booking,Message
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import Site_user
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User 


def index(request):
    a=Service.objects.all()

    if request.method == "POST":
          if "search" in request.POST:
           query=request.POST.get('searchquery')
           a=Service.objects.filter(Q(name__icontains=query)|Q(provider__icontains=query)|Q(address__icontains=query))

    context = {
        "service":a
        } 
    return render(request, 'index.html', context) 


def view_service(request, pk):
    service = get_object_or_404(Service, id=pk)
    comments = service.comments.order_by('-created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                service=service,
                user=request.user,
                content=content
            )
            return redirect('view_service', pk=service.id)
        else:
            messages.error(request, 'Comment cannot be empty.')

    context = {
        "service": service,
        "comments": comments,
    }
    return render(request, 'view_service.html', context)

#profile----------------------

def profile(request):
    try:
        services = Service.objects.filter(user=request.user)
        
        if not services:
            message = "No services found."
        else:
            message = None  
        
        context = {
            'services': services,
            'message': message
        }
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error fetching services: {str(e)}")
        context = {
            'services': None,
            'message': "Error fetching services. Please try again later."
        }
    
    return render(request, 'profile.html', context)


#request---------------
def request(request):
   
    bookings = Booking.objects.filter(service__user=request.user)
    
    context = {
        'bookings': bookings  
    }
    
    return render(request, 'request.html', context)

#view request--------------------

def view_request(request,id):
    a=Booking.objects.get(id=id)
    return render(request,"view_request.html",{"bookings":a})



#acceept booking--------

def accept_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.status = Booking.ACCEPTED 
    booking.save()
    # return redirect('view_request', id=id)
    return redirect("request")




def reject_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.status = Booking.REJECTED  
    booking.save()
    # return redirect('view_request', id=id)
    return redirect("request")


#booking---------------------

@login_required(login_url='login')
def bookings(request):
    user_bookings = Booking.objects.filter(user_profile=request.user.site_user)
    return render(request, "booked.html", {'bookings': user_bookings})

#about-----------------------

def about(request):
    context = {}  
    return render(request, 'about.html', context) 

def services(request):
    context = {}  
    return render(request, 'services.html', context) 

def servicedetail(request):
    context = {} 
    return render(request, 'serviceDetail.html', context) 

def providerpnl(request):
    context = {}  
    return render(request, 'providerpnl.html', context) 


#profile edit--------------

def profile_edit(request, id):
    service = Service.objects.get(id=id)

    if request.method == "POST":
        service.name = request.POST.get("name")
        service.provider = request.POST.get("provider")
        service.description = request.POST.get("description")
        service.price_per_hour = request.POST.get("price_per_hour")
        service.address = request.POST.get("address")
        
        if 'image' in request.FILES:
            service.image = request.FILES['image']
        
        service.save()
        return redirect("profile")

    context = {
        "service": service
    }
    return render(request, "profile_edit.html", context)

#Messages-----------------

@login_required(login_url='login')
def message(request):
    sent_messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messages.html', {'sent_messages': sent_messages, 'received_messages': received_messages})


def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if message.receiver == request.user and not message.read:
        message.read = True
        message.save()
    return render(request, 'message_detail.html', {'message': message})



def compose_message(request):
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver')
        content = request.POST.get('content')
        
        try:
            receiver = User.objects.get(username=receiver_username)
            message = Message.objects.create(
                sender=request.user,
                receiver=receiver,
                content=content
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('messages')  
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
    
    return render(request, 'compose_message.html')

#Book--------------
@login_required(login_url='login')
def book(request):
    if request.method == 'POST':
        place = request.POST.get('place')
        date = request.POST.get('date')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        requirements = request.POST.get('requirements')
        
        if not (place and date and email and mobile):
            messages.error(request, 'Please fill out all required fields.')
            return render(request, 'booking_form.html')
        
        try:
            service_id = request.GET.get('service_id')
            service = Service.objects.get(id=service_id)
            

            booking = Booking.objects.create(
                place=place,
                date=date,
                email=email,
                mobile_number=mobile,
                requirements=requirements,
                user_profile=request.user.site_user, 
                service=service,
                status=Booking.PENDING  
            )
            
            messages.success(request, 'Booking request submitted successfully.')
            return redirect('view_service', pk=service.id)
            
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')
            return render(request, 'booking_form.html')
    
    return render(request, 'booking_form.html')
