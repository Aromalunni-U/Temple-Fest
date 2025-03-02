from django.db import models
from django.contrib.auth.models import User



class Site_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    mobile_number = models.BigIntegerField()
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.user:  
            self.user = User.objects.create_user(username=self.email, email=self.email)
        elif self.user.email != self.email: 
            self.user.email = self.email  
            self.user.save()  
        super().save(*args, **kwargs)
    