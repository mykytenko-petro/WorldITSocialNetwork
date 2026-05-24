from django.views.generic.base import View
from django.http import HttpRequest, JsonResponse

from .forms import ProfileDetailForm


class ProfileDetailView(View):
    def post(self, request: HttpRequest):
        form = ProfileDetailForm(request.POST)

        if form.is_valid():
            request.user.username = form.cleaned_data["username"]
            request.user.profile.author_pseudonym = form.cleaned_data["author_pseudonym"] # type: ignore

            request.user.save()
            request.user.profile.save() # type: ignore

            return JsonResponse({})

        return JsonResponse({"errors": form.errors.get_json_data()}, status=400)