from django.contrib import admin
from django.urls import path, include
from trng.views import index  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('trng.urls')),
    path('', index),  # Add this line
]
