from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from board.models import Ad


@receiver(post_save, sender=Ad)
def send_ad_notification(sender, instance, created, **kwargs):
    """Sends an email notification when a new ad is created.

    This signal receiver listens for the post_save signal on the Ad model.
    If a new ad is created, it sends an email notification to the ad's user.
    """
    if created:
        send_mail(
            "Нове оголошення",
            f'Ваше оголошення "{instance.title}" було успішно створено.',
            "zyamileva@ukr.net",
            [instance.user.email],
            fail_silently=True,
        )
