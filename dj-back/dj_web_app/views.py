from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Booking
from .serializer import BookingSerializer
# Create your views here.
def home(request):
    ids = BookingSerializer.populate_db()
    return HttpResponse("yahallo!\n"+ids)

def create_booking(request):
    """
    Create a new booking or retrieve all bookings.
    """
    if request.method == 'POST':
        # Extract data from the request
        data = request.POST
        print("Data received:", data)
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Booking created successfully!"}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    elif request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)
    
def booking_views(request, pk):
    if request.method == 'GET':
        booking = Booking.objects.filter(booking.id == pk)