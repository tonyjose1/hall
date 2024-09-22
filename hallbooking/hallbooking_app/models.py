# hallbooking_app/models.py
from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255, default="perumbavoor")  # This field should be present
    description = models.TextField(blank=True, null=True)
    amenities = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class UserContact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

# class Booking(models.Model):
#     hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     user_contact = models.ForeignKey(UserContact, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Booking for {self.hall.name} by {self.user_contact.name}"

# # hallbooking_app/models.py

class Booking(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_contact = models.ForeignKey(UserContact, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_details = models.CharField(max_length=255, blank=True)  # Can keep for reference if needed
    event_description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.hall.name} booked for {self.event_type}"

