from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('decrypt_text_code', views.decrypt_text_code, name='decrypt_text_code'),
    path('decrypt_audio', views.decrypt_audio, name='decrypt_audio')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)