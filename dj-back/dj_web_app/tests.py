from django.test import TestCase
from .models import Booking
from random import randint
from datetime import datetime, timedelta


class BookingTestCase(TestCase):
    def setUp(self):
        """
        Create a booking instance for testing.
        """
        
        Booking.objects.create(
            userid=1,
            from_station=2,
            destination_station=3,
            trainid=4,
            boarding_date='2023-10-01', 
            no_of_passengers=5
        )

    def test_booking_creation(self):
        """
        Test that a booking instance is created correctly.
        """
        booking = Booking.objects.get(userid=1)
        self.assertEqual(booking.from_station, 2)
        self.assertEqual(booking.destination_station, 3)
        self.assertEqual(booking.trainid, 4)
        self.assertEqual(booking.no_of_passengers, 5)
            
