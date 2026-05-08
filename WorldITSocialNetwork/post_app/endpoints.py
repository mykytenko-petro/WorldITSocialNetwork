from django.views import View
from django.http import JsonResponse, HttpRequest

from .forms import PostCreationForm


class PostCreationView(View):
    def post(self, request: HttpRequest):
        form = PostCreationForm(data=request.POST)
        # print(form.data)
        if form.is_valid():
            form.save(request.user)

            return JsonResponse({})
        
        else:
            return JsonResponse({
                'errors': form.errors.get_json_data()
            }, status=400)