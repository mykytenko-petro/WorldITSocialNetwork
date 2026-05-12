from django.views import View
from django.http import JsonResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.template.loader import render_to_string
from django.core.paginator import Paginator

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

class PostProviderView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_app/posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def post(self, request: HttpRequest):
        mode = request.POST.get("mode")

        print(request.POST)
        if mode == "own_posts":
            queryset = Post.objects.filter(author_id=self.request.user)
        elif mode == "recommendations":
            queryset = Post.objects.all()
        else:
            return JsonResponse({"errors": "wrong mode"}, status=400)

        paginator = Paginator(queryset, self.paginate_by)

        page_number = request.POST.get('page')
        page_obj = paginator.get_page(page_number)
        
        if int(page_number) > paginator.num_pages: # type: ignore
            return JsonResponse({
                "errors": "congrats you have scrolled to the end!"
            }, status=204)
        
        return JsonResponse({
            'html': render_to_string(
                'post_app/components/show_posts.html',
                {'posts': page_obj.object_list}
            )
        })