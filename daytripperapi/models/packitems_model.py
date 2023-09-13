from django.db import models


class PackItem(models.Model):
    planner = models.ForeignKey(
        "Planner", on_delete=models.CASCADE, related_name='items')
    item_type = models.ForeignKey(
        "ItemType", on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=50)
    amount = models.IntegerField()
    description = models.CharField(max_length=150)
    trips = models.ManyToManyField("Trip", through="PackList")