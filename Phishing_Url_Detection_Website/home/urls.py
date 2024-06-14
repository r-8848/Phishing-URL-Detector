from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detect-phishing/', views.detect_phishing, name='detect_phishing'),
]
