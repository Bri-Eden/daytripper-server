from django.db import models


class ActivityType(models.Model):
    type = models.CharField(max_length=30)
