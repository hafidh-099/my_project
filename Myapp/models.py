from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now


# Student Model
class Student(models.Model):
    first_name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    in_date = models.DateField(default=now)
    out_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Room Model
class Room(models.Model):
    status ={
        'S':'Single',
        'M': 'Marry'
    }
    MarritalStatus = models.CharField(max_length=20, choices=status)
    room_number = models.CharField(max_length=10, unique=True)
    occupied = models.IntegerField(default=0)
    Students = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Room {self.room_number}"
    
# Payment Model
class Payment(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"Fee for {self.students} - {'Paid' if self.paid else 'Unpaid'}"

    
# Complaint Model
class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    complaint = models.TextField()
    submitted_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"Complaint by {self.student}"
