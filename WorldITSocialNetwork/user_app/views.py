from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib import messages

from .forms import RegisterForm, LoginForm, ConfirmEmailForm


User = get_user_model()


class AuthTemplateView(TemplateView):
    template_name = 'user_app/auth.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['form_register'] = RegisterForm()
        context['form_login'] = LoginForm()
        context['form_confirm_email'] = ConfirmEmailForm()
        return context


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            return redirect('auth')

        return redirect('auth')
    
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import login

from .forms import LoginForm


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
        

        return redirect('auth')
    
    #Який ще алгоритм скриптс
    #да я сам не особо понимаю
    #:(