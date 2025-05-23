from django.urls import path
from .views import AdvertisementList


urlpatterns = [
    # Адрес страницы со всеми постами
    path('',
         AdvertisementList.as_view(),
         name='advertisement_list'),
]