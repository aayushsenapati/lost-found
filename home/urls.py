from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('find',views.find),
    path('report',views.report),
    path('reported',views.reported),
    path('success', views.success, name='success'),
    path('thankyou', views.thankyou, name='thankyou')


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)