from django.db import models


class TransportationType(models.Model):
    type = models.CharField(max_length=30)
