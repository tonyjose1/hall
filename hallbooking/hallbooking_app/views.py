from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import HallForm, UserContactForm,BookingForm
from .models import Hall, Booking, UserContact 
from django.utils import timezone
import logging
import random
from django.urls import reverse
from django.core.mail import send_mail
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'hallbooking_app/home.html')

def add_hall(request):
    if request.method == 'POST':
        form = HallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HallForm()
    return render(request, 'hallbooking_app/add_hall.html', {'form': form})

# def book_hall(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         number = request.POST.get('number')
#         email = request.POST.get('email')
#         otp = generate_otp()
#         request.session['otp'] = otp
#         request.session['email'] = email
#         send_otp(email,otp)
#         messages.success(request, 'OTP has been sent to your email.')
#         address=request.POST.get('address')
#         hall_id = request.POST.get('hall')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         event_type = request.POST.get('event_type')
#         event_details = request.POST.get('event_details') if event_type == 'others' else None
#         event_description = request.POST.get('event_description')

#         # Save user contact
#         user_contact = UserContact.objects.create(name=name, number=number, email=email, address=address,)

#         # Create the booking
#         booking = Booking.objects.create(
#             hall_id=hall_id,
#             start_time=start_time,
#             end_time=end_time,
#             user_contact=user_contact,
#             event_type=event_details if event_type == 'others' else event_type,
#             event_description=event_description
#         )

#         return redirect(reverse('booking_confirmation', kwargs={'booking_id': booking.id}))

#     else:
#         halls = Hall.objects.all()  # Get all halls for dropdown
#         return render(request, 'hallbooking_app/book_hall.html', {'halls': halls})



from django.shortcuts import render
from .models import Booking

def check_availability(request):
    bookings = Booking.objects.select_related('hall', 'user_contact').all()  # Fetch all bookings with related hall and user
    return render(request, 'hallbooking_app/check_availability.html', {'bookings': bookings})

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import UserContact, Booking, Hall

# def book_hall(request):
#     if request.method == 'POST':
#         # If the user has entered an OTP
#         if 'otp' in request.POST:
#             if verify_otp(request):
#                 # OTP is verified, proceed with the booking
#                 name = request.POST.get('name')
#                 number = request.POST.get('number')
#                 address = request.POST.get('address')
#                 hall_id = request.POST.get('hall')
#                 start_time = request.POST.get('start_time')
#                 end_time = request.POST.get('end_time')
#                 event_type = request.POST.get('event_type')
#                 event_details = request.POST.get('event_details') if event_type == 'others' else None
#                 event_description = request.POST.get('event_description')

#                 # Save user contact
#                 user_contact = UserContact.objects.create(
#                     name=name, number=number, email=request.session['email'], address=address
#                 )

#                 # Create the booking
#                 booking = Booking.objects.create(
#                     hall_id=hall_id,
#                     start_time=start_time,
#                     end_time=end_time,
#                     user_contact=user_contact,
#                     event_type=event_details if event_type == 'others' else event_type,
#                     event_description=event_description
#                 )

#                 return redirect(reverse('booking_confirmation', kwargs={'booking_id': booking.id}))

#             else:
#                 messages.error(request, 'Invalid OTP. Please try again.')
        
#         else:
#             # First step: user enters email, generate OTP and send
#             email = request.POST.get('email')
#             otp = generate_otp()
#             print(otp)
#             request.session['otp'] = otp
#             request.session['email'] = email
#             send_otp(email, otp)
#             messages.success(request, 'OTP has been sent to your email.')

#     halls = Hall.objects.all()  # Get all halls for dropdown
#     return render(request, 'hallbooking_app/book_hall.html', {'halls': halls})

# def book_hall(request):
#     if request.method == 'POST':
#         # If the user has entered an OTP
#         if 'otp' in request.POST:
#             if verify_otp(request).get('success'):
#                 # OTP is verified, proceed with the booking
#                 name = request.POST.get('name')
#                 number = request.POST.get('number')
#                 address = request.POST.get('address')
#                 hall_id = request.POST.get('hall')
#                 start_time = request.POST.get('start_time')
#                 end_time = request.POST.get('end_time')
#                 event_type = request.POST.get('event_type')
#                 event_details = request.POST.get('event_details') if event_type == 'others' else None
#                 event_description = request.POST.get('event_description')

#                 # Save user contact
#                 user_contact = UserContact.objects.create(
#                     name=name, number=number, email=request.session['email'], address=address
#                 )

#                 # Create the booking
#                 booking = Booking.objects.create(
#                     hall_id=hall_id,
#                     start_time=start_time,
#                     end_time=end_time,
#                     user_contact=user_contact,
#                     event_type=event_details if event_type == 'others' else event_type,
#                     event_description=event_description
#                 )

#                 return redirect(reverse('booking_confirmation', kwargs={'booking_id': booking.id}))

#             else:
#                 messages.error(request, 'Invalid OTP. Please try again.')

#         else:
#             # First step: user enters email, generate OTP and send
#             print("pleej")
#             send_otp(request)
#             messages.success(request, 'OTP has been sent to your email.')

#     halls = Hall.objects.all()  # Get all halls for dropdown
#     return render(request, 'hallbooking_app/book_hall.html', {'halls': halls})

from django.contrib import messages

def book_hall(request):
    if request.method == 'POST':
        # If the user has entered an OTP
        if 'otp' in request.POST:
            otp_response = verify_otp(request)
            if otp_response.get('success'):
                # OTP is verified, proceed with the booking
                name = request.POST.get('name')
                number = request.POST.get('number')
                address = request.POST.get('address')
                hall_id = request.POST.get('hall')
                start_time = request.POST.get('start_time')
                end_time = request.POST.get('end_time')
                event_type = request.POST.get('event_type')
                event_details = request.POST.get('specify') if event_type == 'others' else None
                event_description = request.POST.get('event_description')

                # Save user contact
                user_contact = UserContact.objects.create(
                    name=name, number=number, email=request.session['email'], address=address
                )

                # Create the booking
                booking = Booking.objects.create(
                    hall_id=hall_id,
                    start_time=start_time,
                    end_time=end_time,
                    user_contact=user_contact,
                    event_type=event_details if event_type == 'others' else event_type,
                    event_description=event_description
                )

                return redirect(reverse('booking_confirmation', kwargs={'booking_id': booking.id}))

            else:
                messages.error(request, 'Invalid OTP. Please try again.')

        else:
            # First step: user enters email, generate OTP and send
            send_otp(request)
            messages.success(request, 'OTP has been sent to your email.')

    halls = Hall.objects.all()  # Get all halls for dropdown
    return render(request, 'hallbooking_app/book_hall.html', {'halls': halls})


def booking_confirmation(request, booking_id):
    # Fetch the booking details using the booking_id
    booking = get_object_or_404(Booking, id=booking_id)
    user = booking.user_contact
    print(user)
    
    # Pass the booking details to the template
    return render(request, 'hallbooking_app/booking_confirmation.html', {'booking': booking,'user': user,})


def list_halls(request):
    halls = Hall.objects.all()  # Fetch all halls from the database
    return render(request, 'hallbooking_app/list_halls.html', {'halls': halls})

def generate_otp():
    """Generate a 6-digit OTP"""
    return random.randint(100000, 999999)

# def send_otp(email, otp):
#     """Send the OTP to the provided email"""
#     subject = "Your OTP for Hall Booking"
#     message = f"Your OTP code is {otp}. Please enter this code to proceed with the booking."
#     email_from = 'tonyjosek7@gmail.com'  # Replace with your email
#     recipient_list = [email]
#     print("ok")
#     send_mail(subject, message, email_from, recipient_list)
#     return redirect('book_hall')

def send_otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        #email = request.POST.get('email')
        print(email)
        otp = generate_otp()
        # Save OTP and email in session
        request.session['otp'] = otp
        print(request.session['otp'])
        request.session['email'] = email

        # Send OTP via email (assuming you have email settings configured)
        send_mail(
            'Your OTP for Hall Booking',
            f'Your OTP is {otp}. It is valid for 10 minutes.',
            'no-reply@hallbooking.com',
            [email],
            fail_silently=False,
        )
        print(f"Sending OTP {otp} to {email}")
        return JsonResponse({'success': True, 'message': 'OTP sent successfully'})
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)



# def verify_otp(request):
#     entered_otp = request.POST.get('otp')
#     print(entered_otp)
#     if entered_otp == request.session.get('otp'):
#         return True
#     return False


def verify_otp(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)  # Load the JSON data from the request body
        entered_otp = data.get('otp')  # Get the OTP from the JSON data
        session_otp = request.session.get('otp')
        print(entered_otp)
        print(session_otp)
        if entered_otp != session_otp:
            
            print("ok")
            return JsonResponse({'success': True, 'message': 'OTP verified successfully'})

        else:
            print("no")
            return JsonResponse({'success': False, 'message': 'OTP is incorrect'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)