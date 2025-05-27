from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, MetodoDePagoForm, PedidoForm, BusquedaProductoForm
from .models import Producto

def home(request):
    return render(request, 'Tienda/home.html')

def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'Tienda/crear_producto.html', {'form': form})

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'Tienda/crear_cliente.html', {'form': form})

def crear_metodo_pago(request):
    form = MetodoDePagoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'Tienda/crear_metodo_pago.html', {'form': form})

def crear_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'Tienda/crear_pedido.html', {'form': form})

def buscar_producto(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaProductoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Producto.objects.filter(nombre__icontains=nombre)
    else:
        form = BusquedaProductoForm()
    return render(request, 'Tienda/buscar_producto.html', {'form': form, 'resultados': resultados})
