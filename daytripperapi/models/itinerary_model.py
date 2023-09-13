from django.db import models


class TripActivity(models.Model):
    trip = models.ForeignKey(
        "Trip", on_delete=models.CASCADE, related_name='itinerary')
    activity = models.ForeignKey("Activity", null=True, blank=True,
                              on_delete=models.CASCADE, related_name='itinerary')
