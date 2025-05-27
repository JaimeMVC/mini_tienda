from django import forms
from .models import Producto, Cliente, MetodoDePago, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class MetodoDePagoForm(forms.ModelForm):
    class Meta:
        model = MetodoDePago
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'metodo_pago']  # excluye fecha automática

class BusquedaProductoForm(forms.Form):
    nombre = forms.CharField(label='Buscar producto por nombre', max_length=100)
