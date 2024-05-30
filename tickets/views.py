from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, Image
from .serializers import TicketSerializer, ImageSerializer
from .tasks import upload_image_to_cloudinary
from django.db.models import Count

class CreateTicketView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UploadImageView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        ticket_id = request.data.get('ticket')
        ticket = Ticket.objects.get(id=ticket_id)

        if ticket.status == 'completed':
            return Response({"error": "Ticket is already completed"}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        image = Image.objects.get(id=response.data['id'])

        # Llama a la tarea de Celery para subir la imagen a Cloudinary
        upload_image_to_cloudinary.delay(image.id, request.data.get('image_file'))

        return response

class TicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

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