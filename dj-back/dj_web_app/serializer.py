from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    """
    userid = serializers.IntegerField()
    from_station = serializers.IntegerField()
    destination = serializers.IntegerField()
    trainid = serializers.IntegerField()
    boarding_date = serializers.DateField()
    no_of_passengers = serializers.IntegerField()

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)
    
    
    
    def update(self, instance, validated_data):
        instance.userid = validated_data.get('userid', instance.userid)
        instance.from_station = validated_data.get('from_station', instance.from_station)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.trainid = validated_data.get('trainid', instance.trainid)
        instance.boarding_date = validated_data.get('boarding_date', instance.boarding_date)
        instance.no_of_passengers = validated_data.get('no_of_passengers', instance.no_of_passengers)
        instance.save()
        return instance
    
    def populate_db():
        """
        populates db with random values.

        returns:
            list of ids for deletion.
        """
        from random import randint
        ids = []

        for _ in range(10):
            userId = randint(1,100)
            fromStation = randint(1,100)
            destination = randint(1,100)
            trainId = randint(1,100)
            boardingDate = '2024-10-10'
            noOfPassengers = randint(1,5)
            booking = Booking.objects.create(
                userid=userId, from_station=fromStation, destination_station=destination, trainid=trainId,
                  boarding_date=boardingDate, no_of_passengers=noOfPassengers
            )
            serializer = BookingSerializer(booking)
            ids.append(serializer.data)
        return ids