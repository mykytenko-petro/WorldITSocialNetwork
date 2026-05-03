import random

from django.views import View
from django.contrib.auth import get_user_model, login, authenticate
from django.http import HttpRequest, JsonResponse

from WorldITSocialNetwork.store import cache_store
from .forms import LoginForm, RegisterForm, ConfirmEmailForm
from .smtp import send_code


User = get_user_model()

class RegisterView(View):
    def post(self, request: HttpRequest):
        form = RegisterForm(request.POST)

        if form.is_valid():
            code = random.randint(100000, 999999)

            cache_store[form.cleaned_data["email"]] = {
                "password": form.cleaned_data["password"],
                "code": code
            }

            print("CODE:", code)
            send_code(code, form.cleaned_data["email"])

            return JsonResponse({
                "email": form.cleaned_data["email"]
            })
            
        return JsonResponse({
            'errors': form.errors.get_json_data()
        }, status= 400)

class LoginView(View):
    def post(self, request: HttpRequest):
        form = LoginForm(data=request.POST)
        print(request.POST)

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user:
            login(request, user)
            return JsonResponse({})
        
        return JsonResponse({
            'errors': form.errors.get_json_data()
        })
    
class ConfirmEmailView(View):
    def post(self, request: HttpRequest):
        print(request.POST)
        form = ConfirmEmailForm(data=request.POST)
        
        if not form.is_valid():
            return JsonResponse({
                'errors': form.errors.get_json_data()
            }, status= 400)
        
        if not cache_store.get(form.cleaned_data["email"]):
            return JsonResponse({
                'errors': "немає такої пошти"
            }, status= 400)

        if cache_store[form.cleaned_data["email"]]["code"] != form.code:
            print("Hell nah", cache_store[form.cleaned_data["email"]]["code"], form.code)

            return JsonResponse({
                'errors': "невірний код"
            }, status= 400)
        
        User.objects.create_user(
            username=" ",
            email=form.cleaned_data['email'],
            password=cache_store[form.cleaned_data["email"]]["password"]
        )

        return JsonResponse({})