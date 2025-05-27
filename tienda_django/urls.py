from django.contrib import admin
from django.urls import path, include  # importamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tienda.urls')),  # conectamos las URLs de la app
]
