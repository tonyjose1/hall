# hallbooking_app/admin.py
from django.contrib import admin
from .models import Hall, Booking,UserContact

admin.site.register(Hall)
admin.site.register(Booking)
admin.site.register(UserContact)