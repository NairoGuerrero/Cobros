from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django_datatables_view.base_datatable_view import BaseDatatableView


@login_required
def home(request):
    return render(request, "principal/home.html")

@login_required
def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cobros_app:lista_clientes")  # Redirige a la lista de clientes
    else:
        form = ClienteForm()

    return render(request, "principal/cliente/crear_cliente.html", {"form": form})

class ClientesList(BaseDatatableView):
    model = Cliente

    def render_column(self, row, column):
        return super().render_column(row, column)

    def filter_queryset(self, qs):
        return qs

    def prepare_results(self, qs):
        data = []
        for item in qs:
            data.append(
                {
                    "id": item.id,
                    "nombre": item.nombre,
                    "alias": item.alias,
                    "is_active": item.activo,
                    "ciudad": item.get_ciudad_display(),
                    "direccion": item.direccion,
                    "telefono": item.telefono,
                    "puntuacion": item.get_puntuacion_display(),
                }
            )
        return data


@login_required
def lista_clientes(request):
    return render(request, "principal/cliente/lista_clientes.html")