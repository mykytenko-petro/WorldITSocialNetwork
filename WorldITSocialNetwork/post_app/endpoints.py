from django.views import View
from django.http import JsonResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostCreationForm
from .models import Tag

class PostCreationView(View):
    def post(self, request: HttpRequest):
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user) # type: ignore

            return JsonResponse({})
        
        else:
            return JsonResponse({
                'errors': form.errors.get_json_data()
            }, status=400)
            
class TagCreationView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest):
        name = request.POST.get('name', '')

        if not name:
            return JsonResponse({
                'errors': {
                    'name': [{'message': 'Введіть назву хештегу'}]
                }
            }, status=400)
        
        tag = Tag.objects.create(name=name)
        
        return JsonResponse({'id': tag.pk,'name': tag.name})

