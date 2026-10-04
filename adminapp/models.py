from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    admin_pic = models.ImageField(upload_to="admin/",default="admin.jpeg")

    def __str__(self):
        return self.username

class Room(models.Model):
    room_no = models.CharField(max_length=200,unique=True)
    floor = models.PositiveIntegerField()
    room_type = models.CharField(max_length=100)
    total_beds = models.PositiveIntegerField()
    monthly_rent = models.DecimalField(max_digits=10,decimal_places=2)
    room_image = models.ImageField(upload_to="rooms/")
    description = models.TextField()
    rating = models.PositiveIntegerField()
    review = models.TextField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.room_no

class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_no = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.room.room_no}->{self.bed_no}"

class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
