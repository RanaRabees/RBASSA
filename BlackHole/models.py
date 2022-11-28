from django.db import models

# Create your models here.

class RBSAUserForm(models.Model):
    name=models.CharField(max_length=50,default="")
    father_name=models.CharField(max_length=50,default="")
    age=models.CharField(max_length=50,default="")
    password=models.CharField(max_length=50,default="")
    howmany=models.CharField(max_length=50,default="")
    cardnumber=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    gender=models.CharField(max_length=50,default="")
    about_you=models.TextField()
    user_image=models.FileField(upload_to="User_Images",default="")
    DOB=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name  

class UserFormpy(models.Model):
    name=models.CharField(max_length=50,default="")
    father_name=models.CharField(max_length=50,default="")
    age=models.CharField(max_length=50,default="")
    password=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    gender=models.CharField(max_length=50,default="")
    about_you=models.TextField()
    user_image=models.FileField(upload_to="FormsData",default="")
    DOB=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name  

class SimpleUserFormOne(models.Model):
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    password=models.CharField(max_length=50,default="")
    age=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name  