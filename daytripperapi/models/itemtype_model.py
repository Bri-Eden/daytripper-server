from django.db import models


class ItemType(models.Model):
    type = models.CharField(max_length=30)