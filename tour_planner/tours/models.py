from django.db import models

class TourLeg(models.Model):
    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=200)
    venue_city = models.CharField(max_length=50)
    venue_state = models.CharField(max_length=20)
    venue_lat = models.FloatField(blank=True, null=True)
    venue_lng = models.FloatField(blank=True, null=True)
    notes = models.TextField()
    gig_date = models.DateField()
    gig_start = models.CharField(max_length=10)
    gig_length = models.IntegerField(default=0)
    pay = models.IntegerField()
    
    def __str__(self):
        return f'{self.venue_name} - {self.gig_date}'
