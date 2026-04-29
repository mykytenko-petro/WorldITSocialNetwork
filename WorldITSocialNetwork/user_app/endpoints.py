from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, login, authenticate
from django import forms
from django.http import JsonResponse

from .forms import LoginForm, RegisterForm, ConfirmEmailForm


User = get_user_model()

class RegisterView(View):
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            
            User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return JsonResponse({
                "success": True,
                'errors': form.errors.get_json_data()
        })
            
        return JsonResponse({
            'success': False,
            'errors': form.errors.get_json_data()
        }, status= 400)
        
        

class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user:
            login(request, user)
            print("hello register")
            return redirect('/')
        
        return JsonResponse({
            "success": True,
            'errors': form.errors.get_json_data()
        })
    
class ConfirmView(View):
    def post(self, request, *args, **kwargs):
        form = ConfirmEmailForm(data=request.POST)
        
        if form is not form.is_valid():
            return JsonResponse({
                'success': False,
                'errors': form.errors.get_json_data()
            }, status= 400)
        
        return JsonResponse({
            "success": True,
            'errors': form.errors.get_json_data()
        })
        