from django.db import models

class User(models.Model):
  username = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=50)
  password = models.CharField(max_length=200)
  
  def __str__(self):
    return self.username
  
class UserProfile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  city = models.CharField(max_length=100)
  pincode = models.CharField(max_length=50)
  state = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  address = models.TextField()
  bio = models.TextField()
  aadhar_no = models.BigIntegerField()
  aadhar_image = models.ImageField(upload_to="proof/")
  profile_pic = models.ImageField(upload_to="users/")
  
  def __str__(self):
    return f"{self.user.username} Profile"