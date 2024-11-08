from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('map.urls')),  # Now your map view is accessible at the root URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
