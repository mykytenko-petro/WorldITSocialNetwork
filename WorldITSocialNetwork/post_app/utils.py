from io import BytesIO

from PIL import Image
from django.core.files import File
from django.core.files.base import ContentFile


IMAGE_SIZE_THRESHOLD = 2 * 1024 ** 2

def compress_image(image: File):
    image.seek(0)

    image_compressed = Image.open(image)
    image_compressed = image_compressed.convert('RGB')

    quality = 85
    width, height = image_compressed.size

    while True:
        buffer = BytesIO()

        image_compressed.save(
            fp=buffer, 
            format='JPEG',
            quality=quality,
            optimize=True
        )

        if buffer.tell() <= IMAGE_SIZE_THRESHOLD:
            break

        if width <= 1 or height <= 1:
            break

        if quality > 35:
            quality -= 10

        else:
            width = int(width * 0.9)
            height = int(height * 0.9)
            
            image_compressed = image_compressed.resize(
                size=(width, height),
                resample=Image.Resampling.LANCZOS
            )           
            
    image.seek(0)
    
    name_compressed = f'compressed_{image.name.rsplit('.', 1)[0]}.jpeg'

    return ContentFile(buffer.getvalue(), name=name_compressed)