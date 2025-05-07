from django.db import models

# Create your models here.
class Booking(models.Model):
    """
    represents db table 'Bookings' 
    """
    id = models.AutoField(primary_key=True, auto_created=True)
    userid = models.IntegerField()
    from_station = models.IntegerField()
    destination_station = models.IntegerField()
    trainid = models.IntegerField()
    boarding_date = models.DateField()
    no_of_passengers = models.IntegerField()

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.id
    
    
        