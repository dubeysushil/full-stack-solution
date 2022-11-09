from django.db import models

# Create your models here.

class TeamMember(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.PositiveBigIntegerField()
    TYPE_SELECT = (
        ('Regular', "Regular - Can't delete members"),
        ('Admin', "Admin - Can delete members"),
    )
    role = models.CharField(max_length=50,choices=TYPE_SELECT, default='Regular')
    
    def __str__(self):
        return "%s %s %s %s" %(self.firstName, self.lastName, self.email, self.phoneNumber)