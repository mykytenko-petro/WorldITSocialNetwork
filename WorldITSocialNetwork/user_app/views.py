from django.views.generic.base import TemplateView

from .forms import RegisterForm, LoginForm, ConfirmEmailForm

class AuthTemplateView(TemplateView):
    template_name = 'user_app/auth.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['form_register'] = RegisterForm()
        context['form_login'] = LoginForm()
        context['form_confirm_email'] = ConfirmEmailForm()
        return context


