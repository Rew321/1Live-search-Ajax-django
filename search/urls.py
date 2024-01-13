
from django.contrib import admin
from django.urls import path
from searchapp import views
from django.conf import settings
from django.conf.urls.static import static
from search.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from searchapp.views import search_result,detail_series
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('search/', search_result, name='search'), 
    path('detail/<int:pk>/', detail_series, name='detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
