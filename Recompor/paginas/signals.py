from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Notification

@receiver(user_logged_in)
def create_login_notification(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    Notification.objects.create(
        user=user,
        message=f"Novo login detectado no IP: {ip}"
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
