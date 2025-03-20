from datetime import timedelta

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.utils.timezone import now
from board.models import Ad
from django.db.models import Count


def get_recent_ads():
    """Retrieves ads created within the last 30 days.

    This function returns a QuerySet of Ad objects that have been created
    within the last 30 days.
    """
    return Ad.objects.filter(created_at__gte=now() - timedelta(days=30))


def get_active_ads_by_category(category_id: str):
    """Retrieves active ads for a specific category.

    This function returns a QuerySet of active Ad objects that belong to the
    specified category ID.
    """
    return Ad.objects.filter(category_id=category_id, is_active=True)

def get_active_ads(request:HttpRequest)->HttpResponse:
    """Retrieves and renders active ads.

    This view function fetches all active ads, orders them by creation date
    (newest first), and renders them using the 'board/ad_list.html' template.
    """
    ads = Ad.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'board/ad_list.html', {'ads': ads})


def get_comments_count_for_each_ad():
    """Annotates each ad with the count of its comments.

    This function returns a QuerySet of Ad objects, each annotated with the
    number of comments associated with it.
    """
    return Ad.objects.annotate(comment_count=Count("comment"))


def get_ads_by_user(user_id: Ad):
    """Retrieves ads created by a specific user.

    This function returns a QuerySet of Ad objects that were created by the
    user with the given user ID.
    """
    return Ad.objects.filter(user_id=user_id)



