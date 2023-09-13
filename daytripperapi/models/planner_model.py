from django.db import models
from django.contrib.auth.models import User


class Planner(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional address field to capture from the client
    location = models.CharField(max_length=155)
    photo = models.URLField()

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
