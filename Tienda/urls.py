from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear-metodo-pago/', views.crear_metodo_pago, name='crear_metodo_pago'),
    path('crear-pedido/', views.crear_pedido, name='crear_pedido'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
]

