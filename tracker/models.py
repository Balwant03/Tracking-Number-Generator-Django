from django.db import models

class TrackingNumber(models.Model):
    number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)