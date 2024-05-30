from celery import shared_task
import requests
from .models import Image

@shared_task
def upload_image_to_storage(image_id):
    image = Image.objects.get(id=image_id)
    # Aquí iría la lógica para subir la imagen a Cloudinary
    # response = requests.post('URL_CLOUDINARY', data={'file': image.image_url})
    # image.image_url = response.json()['secure_url']
    # image.save()
