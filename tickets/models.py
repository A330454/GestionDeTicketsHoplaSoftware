from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_images = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])

class Image(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)