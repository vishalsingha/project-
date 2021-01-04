from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('contact/', views.contact, name = 'contact'),
    path('doctor/', views.doctor, name = 'doctor'),
    path('data_save', views.pic_uploader, name = 'doctor-pic'),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)