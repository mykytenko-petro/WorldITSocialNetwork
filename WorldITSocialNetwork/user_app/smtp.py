from django.core.mail import send_mail

from WorldITSocialNetwork.settings import EMAIL_HOST_USER


def send_code(code, email):
    try:
        send_mail(
        subject="Код підтвердження",
        message=f"Код підтвердження: {code}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
    except: pass