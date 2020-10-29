# from django.contrib import admin
from django.urls import path
# Импортируем Class-base view
from .views import PetsList, PetsDetailView, KindList, AboutUs

#Модули для МЕДИА файлов
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PetsList.as_view()),
    path('<int:pk>', PetsDetailView.as_view(), name='pet-detail'),
    path('<str:kind>', KindList.as_view()),
    path('about/', AboutUs.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

