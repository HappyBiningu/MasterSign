from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Gesture(models.Model):
    """
    Model to store gesture data
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GestureRecognitionResult(models.Model):
    """
    Model to store gesture recognition results
    """
    gesture = models.ForeignKey(Gesture, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gesture.name} - {self.result}"
    