from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^2_1/$', views.page2_1),
    url(r'^2_2/$', views.page2_2),
    url(r'^2_3/$', views.page2_3or4),
    url(r'^2_4/$', views.page2_4),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
