from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, Image
from .serializers import TicketSerializer, ImageSerializer
from .tasks import upload_image_to_cloudinary
from django.db.models import Count
import logging
from rest_framework.pagination import PageNumberPagination

logger = logging.getLogger(__name__)


class CreateTicketView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)
        status = self.request.query_params.get('status')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if status:
            queryset = queryset.filter(status=status)
        if start_date and end_date:
            queryset = queryset.filter(created_at__range=[start_date, end_date])

        return queryset

class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user)

class ImageDetailView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(ticket__user=user)
    
class UploadImageView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        logger.info(f"Received request to upload image with data: {request.data}")
        ticket_id = request.data.get('ticket')
        image_url = request.data.get('image_url')
        
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return Response({"error": "Ticket does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        if ticket.images.count() >= ticket.num_images:
            return Response({"error": "Ticket already has the maximum number of images"}, status=status.HTTP_400_BAD_REQUEST)

        if ticket.status == 'completed':
            return Response({"error": "Ticket is already completed"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear la imagen con estado pendiente
        image = Image.objects.create(ticket=ticket, image_url=image_url, status='pending')

        # Llama a la tarea de Celery para subir la imagen a Cloudinary
        logger.info(f"Sending Information to upload_image_to_cloudinary with ID: {image.id}")
        upload_image_to_cloudinary(image.id)
        logger.info(f"Dispatched Celery task for image ID {image.id}")

        serializer = self.get_serializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)