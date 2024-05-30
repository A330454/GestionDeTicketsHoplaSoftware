from celery import shared_task
import cloudinary.uploader
import logging
from .models import Image

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def upload_image_to_cloudinary(self, image_id):
    logger.info(f"Task upload_image_to_cloudinary started for image ID {image_id}")
    try:
        image = Image.objects.get(id=image_id)
        logger.info(f"Starting upload for image ID {image_id}")
        # Subir la imagen a Cloudinary
        upload_result = cloudinary.uploader.upload(image.image_url)
        logger.info(f"Upload result: {upload_result}")

        image.image_url = upload_result['secure_url']
        image.status = 'completed'
        image.save()

        # Verificar si todas las imágenes del ticket están completadas
        ticket = image.ticket
        if ticket.images.filter(status='completed').count() >= ticket.num_images:
            ticket.status = 'completed'
            ticket.save()
        logger.info(f"Image ID {image_id} uploaded successfully and ticket status updated.")
    except Exception as e:
        logger.error(f"Error uploading image ID {image_id}: {e}")
        image.status = 'error'
        image.save()
        self.retry(exc=e, countdown=60, max_retries=3)
