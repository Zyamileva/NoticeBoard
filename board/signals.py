import logging

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from board.models import Ad

logger = logging.getLogger(__name__)
@receiver(post_save, sender=Ad)
def send_ad_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Нове оголошення",
            f'Ваше оголошення "{instance.title}" було успішно створено.',
            "c37991a19b3a84@inbox.mailtrap.io",
            [instance.user.email],
            fail_silently=True,
        )
