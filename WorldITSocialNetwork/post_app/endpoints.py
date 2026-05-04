from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.views import View
from django.http import JsonResponse
from django.forms.widgets import ClearableFileInput

MAX_SIZE = 5 * 1024 * 1024

def compress_image(image):
    if image.size > MAX_SIZE:
        img = Image.open(image)
        quality = 90
        while True:
            output = BytesIO()
            img.save(output, format=img.format or 'JPEG', quality=quality, optimize=True)
            if output.tell() <= MAX_SIZE or quality <= 10:
                break
            quality -= 5
        
        output.seek(0)
        image = InMemoryUploadedFile(
            file=output,
            field_name='ImageField',
            name=image.name,
            content_type='image/jpeg',
            size=sys.getsizeof(output),
            charset=None
        )
    return image


class EndPoint(View):
    def post(self, request):
        image = request.FILES.get('image')
        if image:
            image = compress_image(image)
        return JsonResponse({'status': 'ok'})