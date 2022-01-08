from django.db import models

# Create your models here.
class BusDetails(models.Model):
    Bus_No = models.IntegerField()
    Departure_Time = models.TimeField()
    Destinations = models.CharField(max_length=1000)
    Seats_Available=models.IntegerField()
    TicketCosts = models.CharField(max_length=1000)


