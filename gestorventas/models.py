from django.db import models

# Create your models here.
class Vendedor(models.Model):
    vendedorId = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ReglaComision(models.Model):
    reglaId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, help_text="Nombre de la regla / meta")
    meta_venta = models.DecimalField(max_digits=12, decimal_places=2, help_text="Meta en dinero")
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje (ej: 5 para 5%)")

    def __str__(self):
        return f"{self.nombre} - {self.porcentaje_comision}%"

class Venta(models.Model):
    ventaId = models.AutoField(primary_key= True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name="ventas")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Venta {self.ventaId} - {self.vendedor} - {self.monto}"