from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Producto
from datetime import datetime

def inicio_caffenio(request):
    # Pasamos la fecha para el footer
    return render(request, 'inicio.html', {'now': datetime.now()})

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        empresa = request.POST.get('empresa', '')
        telefono = request.POST.get('telefono', '')
        correo = request.POST.get('correo', '')
        direccion = request.POST.get('direccion', '')
        pais = request.POST.get('pais', '')
        tipo_producto = request.POST.get('tipo_producto', '')

        Proveedor.objects.create(
            nombre=nombre,
            empresa=empresa,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            pais=pais,
            tipo_producto=tipo_producto
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre', proveedor.nombre)
        proveedor.empresa = request.POST.get('empresa', proveedor.empresa)
        proveedor.telefono = request.POST.get('telefono', proveedor.telefono)
        proveedor.correo = request.POST.get('correo', proveedor.correo)
        proveedor.direccion = request.POST.get('direccion', proveedor.direccion)
        proveedor.pais = request.POST.get('pais', proveedor.pais)
        proveedor.tipo_producto = request.POST.get('tipo_producto', proveedor.tipo_producto)
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', proveedor_id=proveedor.id)

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

def ver_productos(request):
    productos = Producto.objects.select_related('proveedor').all()
    return render(request, 'producto/ver_producto.html', {'productos': productos})

# --- agregar producto
def agregar_producto(request):
    proveedores = Proveedor.objects.all()  # para el select
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        descripcion = request.POST.get('descripcion', '')
        precio = request.POST.get('precio', '0')
        stock = request.POST.get('stock', '0')
        categoria = request.POST.get('categoria', '')
        proveedor_id = request.POST.get('proveedor', None)
        sucursal = request.POST.get('sucursal', '')

        proveedor = None
        if proveedor_id:
            proveedor = Proveedor.objects.filter(id=proveedor_id).first()

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            proveedor=proveedor,
            sucursal=sucursal
        )
        return redirect('ver_productos')

    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

# --- mostrar formulario de actualización
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})

# --- procesar la actualización
def realizar_actualizacion_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre', producto.nombre)
        producto.descripcion = request.POST.get('descripcion', producto.descripcion)
        producto.precio = request.POST.get('precio', producto.precio)
        producto.stock = request.POST.get('stock', producto.stock)
        producto.categoria = request.POST.get('categoria', producto.categoria)
        proveedor_id = request.POST.get('proveedor', None)
        if proveedor_id:
            producto.proveedor = Proveedor.objects.filter(id=proveedor_id).first()
        producto.sucursal = request.POST.get('sucursal', producto.sucursal)
        producto.save()
        return redirect('ver_productos')
    return redirect('actualizar_producto', producto_id=producto.id)

# --- borrar producto (confirmación)
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


