from django.views import View
from django.http import JsonResponse


class EndPoint(View):
    def post(self, request):
        image = request.FILES.get('image')

        return JsonResponse({'status': 'ok'})