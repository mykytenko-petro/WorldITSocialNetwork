from django.core.mail import send_mail

from django.conf import settings


def send_code(code, email):
    try:
        send_mail(
        subject="Код підтвердження",
        message=f"Код підтвердження: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
    except: pass