from .views import get_active_ads
from django.urls import path


urlpatterns = [
    path('', get_active_ads, name='get_active_ads'),

]