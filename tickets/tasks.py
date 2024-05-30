from celery import shared_task
import cloudinary.uploader
from .models import Image, Ticket

@shared_task
def upload_image_to_cloudinary(image_id, image_file):
    image = Image.objects.get(id=image_id)
    try:
        upload_result = cloudinary.uploader.upload(image_file)
        image.image_url = upload_result['secure_url']
        image.status = 'completed'
        image.save()

        # Verifica si todas las imágenes del ticket están completadas
        ticket = image.ticket
        if ticket.images.filter(status='completed').count() >= ticket.num_images:
            ticket.status = 'completed'
            ticket.save()
    except Exception as e:
        image.status = 'error'
        image.save()
        raise e
