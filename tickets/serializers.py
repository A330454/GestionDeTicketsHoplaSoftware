from rest_framework import serializers
from .models import Ticket, Image

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'num_images', 'created_at', 'status']
        read_only_fields = ['user']  # Hacer que user sea de solo lectura

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, "user"):
            user = request.user
            validated_data['user'] = user
        return super(TicketSerializer, self).create(validated_data)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'ticket', 'image_url', 'uploaded_at', 'status']
        read_only_fields = ['status']  # Hacer que status sea de solo lectura