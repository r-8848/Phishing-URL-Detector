from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review_page/', views.review_page, name='review_page'),
    path('detect-phishing/', views.detect_phishing, name='detect_phishing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
