from django.contrib import admin
from .models import Proveedor, Producto, Venta

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'telefono', 'correo', 'pais', 'direccion', 'tipo_producto')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'proveedor', 'sucursal')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'cliente', 'total', 'metodo_pago', 'sucursal', 'empleado')


