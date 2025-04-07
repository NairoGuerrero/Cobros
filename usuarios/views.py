from django.shortcuts import render, redirect
from django.contrib.auth import login
from django_datatables_view.base_datatable_view import BaseDatatableView
from usuarios.models import CustomUser  # Asegúrate de importar el modelo correcto
from Cobros_app.urls import app_name
from .forms import CustomUserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

def registro(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica al usuario después del registro
            return redirect("cobros_app:home")  # Redirige a la página principal o donde prefieras
    else:
        form = CustomUserCreationForm()

    return render(request, "usuarios/registro.html", {"form": form})

# @csrf_exempt
def change_password(request, user_id):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=user_id)
        new_password = request.POST.get('password')
        user.password = make_password(new_password)  # Hashear la contraseña
        user.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


class UsuariosList(BaseDatatableView):
    model = CustomUser

    def render_column(self, row, column):
        return super().render_column(row, column)

    def filter_queryset(self, qs):
        # Filtrar solo los usuarios cuyo tipo sea "cobrador"
        return qs.filter(user_type="cobrador")

    def prepare_results(self, qs):
        data = []
        for item in qs:
            data.append(
                {
                    "id": item.id,
                    "username": item.username,
                    "user_type": item.get_user_type_display(),
                    "is_active": item.is_active,
                }
            )
        return data


@login_required
def lista_usuarios(request):
    return render(request, "usuarios/lista_usuarios.html")

@login_required
def toggle_user_status(request, user_id):
    print('hola')
    if request.method == "POST":
        print('nose')
        user = CustomUser.objects.filter(id=user_id).first()
        user.is_active = not user.is_active  # Cambiar estado activo/inactivo
        user.save()
        return JsonResponse({"success": True, "is_active": user.is_active})
    return JsonResponse({"error": "Método no permitido"}, status=405)