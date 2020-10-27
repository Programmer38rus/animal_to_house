# from django.contrib import admin
from django.urls import path
# Импортируем Class-base view
from .views import PetsList

#Модули для МЕДИА файлов
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base/', PetsList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

