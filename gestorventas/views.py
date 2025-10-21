from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Vendedor, Venta, ReglaComision
from .forms import VentaForm
from django.contrib import messages
from datetime import datetime

def index(request):
    ventas = Venta.objects.all().order_by('-fecha')  # todas las ventas, más recientes primero
    return render(request, 'gestorventas/index.html', {'ventas': ventas})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gestorventas/ventas_exito.html")
    else:
        form = VentaForm()
    return render(request, "gestorventas/registrar_venta.html", {'form': form})

def calcular_bono(request):
    resultado = None
    if request.method == 'POST':
        vendedor_id = request.POST.get('vendedor')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        qs = Venta.objects.all()
        if vendedor_id:
            qs = qs.filter(vendedor_id=vendedor_id)
        if fecha_inicio:
            qs = qs.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            qs = qs.filter(fecha__lte=fecha_fin)

        total = qs.aggregate(total=Sum('monto'))['total'] or 0
        # Aplica reglas: selecciona la regla que cumpla la meta y calcula comisión sumando porcentajes aplicables
        reglas = ReglaComision.objects.all().order_by('-meta_venta')
        bono = 0
        regla_aplicada = None
        for regla in reglas:
            if total >= regla.meta_venta:
                bono = (total * regla.porcentaje_comision) / 100
                regla_aplicada = regla
                break

        resultado = {
            'total': total,
            'bono': bono,
            'regla': regla_aplicada,
            'ventas': qs.order_by('fecha')
        }

    vendedores = Vendedor.objects.all()
    reglas = ReglaComision.objects.all()
    context = {'vendedores': vendedores, 'reglas': reglas, 'resultado': resultado}
    return render(request, "gestorventas/calcular_bono.html", context)