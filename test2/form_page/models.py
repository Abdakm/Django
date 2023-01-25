from django.db import models

# Create your models here.
class Information(models.Model):
	firstname=models.CharField("firstname",max_length=30)
	lastname=models.CharField("lastname",max_length=30)
	email=models.EmailField("email",max_length=30)	
	password=models.CharField("password",max_length=30)
	repassword=models.CharField("repassword",max_length=30)

	def __str__(self):
		return f''' {self.firstname} {self.lastname} '''


class Subjects(models.Model):
	subject_name = models.CharField("Subject Name", max_length=50)
	subject_number = models.CharField("Subject Number", max_length=30)

	def __str__(self):
		return f""" {self.subject_name} : {self.subject_number} """

class StdSubjects(models.Model):
	std_name = models.ForeignKey(Information, blank=False, null=False, on_delete=models.CASCADE)
	subjects = models.ManyToManyField(Subjects, blank=False)

	def __str__(self):
		return f""" {self.std_name} : {self.subjects} """

