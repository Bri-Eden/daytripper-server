from django.db import models


class Trip(models.Model):
    planner = models.ForeignKey(
        "Planner", on_delete=models.CASCADE, related_name='trip')
    mode_of_transport = models.ForeignKey(
        "TransportationType", on_delete=models.CASCADE, related_name='trip')
    cover_photo = models.URLField()
    destination = models.CharField(max_length=50)
    num_of_days = models.IntegerField()
    num_of_nights = models.IntegerField()
    climate = models.CharField(max_length=150)
    arrival = models.DateField()
    departure = models.DateField()
