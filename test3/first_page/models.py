from django.db import models

# Create your models here.
class Std_Info(models.Model):
    firstname = models.CharField("FirstName", max_length=50)
    lastname = models.CharField("LastName", max_length=50)
#    email = models.EmailField("Email", max_length=50)
#    password = models.CharField("Password", max_length=50)
#    repassword = models.CharField("Re-Password", max_length=50)
    
    def __str__(self):
        return f""" {self.firstname} {self.lastname} """