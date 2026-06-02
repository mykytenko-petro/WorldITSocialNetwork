from typing import Any

from django.views import View
from django.http import JsonResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin

from WorldITSocialNetwork.utils import PaginationProvider
from .forms import PostCreationForm
from .models import Tag, Post


class PostCreationView(LoginRequiredMixin, View):
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

class PostProviderView(LoginRequiredMixin, PaginationProvider):
    modes = [
        "own_posts",
        "recommendations"
    ]

    def get(self, request: HttpRequest):
        mode = request.GET.get("mode")
        
        if mode not in self.modes:
            print("mode:", mode)
            return JsonResponse({"errors": "wrong mode"}, status=400)

        self.mode = mode

        return super().get(request)

    @property
    def queryset(self) -> Any:
        match self.mode:
            case "own_posts":
                return Post.objects.filter(author_id=self.request.user)
            case "recommendations":
                return Post.objects.all()

    @property
    def template_name(self) -> str:
        return "post_app/components/show_posts.html"
