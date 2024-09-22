# hallbooking/urls.py
from django.contrib import admin
from django.urls import path
from hallbooking_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list_halls/', views.list_halls, name='list_halls'),
    path('check_availability/', views.check_availability, name='check_availability'),
    path('book_hall/', views.book_hall, name='book_hall'),
    path('add_hall/', views.add_hall, name='add_hall'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
]
