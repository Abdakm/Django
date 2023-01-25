from django.db import models

# Create your models here.

class Information(models.Model):
	First_Name = models.CharField("First Name", max_length=50)
	Last_Name = models.CharField("Last Name", max_length=50)
	Email = models.EmailField("Email")
	Password = models.CharField("Password", max_length=50)
	Re_Password = models.CharField("Re_Password", max_length=50)

	def __str__(self):
		return f""" {self.First_Name} {self.Last_Name} {self.Password} """