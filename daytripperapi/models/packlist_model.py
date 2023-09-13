from django.db import models


class PackList(models.Model):
    packitem = models.ForeignKey(
        "PackItem", on_delete=models.CASCADE)
    trip = models.ForeignKey("Trip", null=True, blank=True,
                                 on_delete=models.CASCADE)
