from django.db import models
from django.contrib.auth.models import User
from account.models import Site_user

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services',null=True,blank=True)
    name = models.CharField(max_length=100)
    provider=models.CharField(max_length=100)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    address=models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='static/service images', default='static/service images/Festiconnect.png')


    def __str__(self):
        return self.name
    

class Comment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.service.name}'


class Booking(models.Model):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]
    
    user_profile = models.ForeignKey(Site_user, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    mobile_number = models.BigIntegerField()
    email = models.EmailField()
    place = models.CharField(max_length=100)  
    requirements = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Booking for {self.service.name} by {self.user_profile.first_name} {self.user_profile.last_name}"
    
class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} to {self.receiver} at {self.timestamp}"