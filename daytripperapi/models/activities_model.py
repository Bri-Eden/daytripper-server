from django.db import models


class Activity(models.Model):
    trip = models.ForeignKey(
        "Trip", on_delete=models.CASCADE, related_name='trip')
    activity_type = models.ForeignKey(
        "ActivityType", on_delete=models.CASCADE, related_name='trip')
    title = models.CharField(max_length=50)
    day = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=200)
