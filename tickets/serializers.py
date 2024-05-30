from rest_framework import serializers
from .models import Ticket, Image

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'num_images', 'created_at', 'status']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'ticket', 'image_url', 'uploaded_at', 'status']
