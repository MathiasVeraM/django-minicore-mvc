from django.contrib import admin
from .models import Vendedor, Venta, ReglaComision

# Register your models here.
admin.site.register(Venta)
admin.site.register(Vendedor)
admin.site.register(ReglaComision)