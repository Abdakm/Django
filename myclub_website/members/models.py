from django.db import models

# Create your models here.

class information(models.Model):
	first_name = models.CharField('First_Name', max_length=100)
	last_name = models.CharField('Last_Name', max_length=100)
	email = models.EmailField('Email Field')

	def __str__(self):
		return f''' Firstname: {self.first_name} Lastname: {self.last_name} Email: {self.EmailField}'''