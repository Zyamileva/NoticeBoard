from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
from .models import Ad


@shared_task
def deactivate_expired_ads():
    """Deactivates ads older than 30 days.

    This task finds all active ads that were created more than 30 days ago
    and sets their is_active status to False.
    """
    expired_ads = Ad.objects.filter(
        is_active=True, created_at__lte=now() - timedelta(days=30)
    )
    expired_ads.update(is_active=False)
    return f"Deactivated {expired_ads.count()} ads"
