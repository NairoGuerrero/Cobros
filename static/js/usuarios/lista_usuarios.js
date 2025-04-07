let tabla_usuarios = $('#usuarios').DataTable({
    responsive: true,
    serverSide: true,
    processing: true,
    searching: false,
    lengthChange: false,
    ordering: false,
    ajax: URL_DATA,
    language: {
        info: "",
        infoFiltered: "",
        infoEmpty: ""
    },
    columns: [
        {data: 'username', title: 'Usuario'},
        {data: 'user_type', title: 'Tipo de Usuario'},
        {
            data: null,
            title: 'Estado',
            render: function(data, type, row) {
                let btnClass = row.is_active ? 'btn-danger' : 'btn-success';
                let btnText = row.is_active ? 'Desactivar' : 'Activar';
                return `<button class="btn ${btnClass}" onclick="toggleUserStatus(${row.id}, ${row.is_active})">${btnText}</button>`;
            }
        },
        {
            data: null,
            title: 'Acciones',
            render: function(data, type, row) {
                return `<button class="btn btn-warning" onclick="openPasswordModal(${row.id})">
                            <i class="bi bi-key"></i> Cambiar Contraseña
                        </button>`;
            }
        }
    ]
});

// Función para activar/desactivar usuario
function toggleUserStatus(userId, isActive) {
    $.ajax({
        url: URL_IS_ACTIVE.replace("0", userId),  // Reemplazar el 0 por el ID del usuario
        method: 'POST',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            is_active: !isActive
        },
        success: function(response) {
            tabla_usuarios.ajax.reload();  // Recargar la tabla después de actualizar el estado
        },
        error: function(error) {
            alert('Error al cambiar el estado del usuario');
        }
    });
}

// Función para abrir el modal de cambio de contraseña
function openPasswordModal(userId) {
    $('#passwordModal').modal('show');
    $('#passwordUserId').val(userId);
}

// Función para cambiar la contraseña
function changeUserPassword() {
    let userId = $('#passwordUserId').val();
    let newPassword = $('#newPassword').val();

    if (!newPassword) {
        Swal.fire({
            icon: 'warning',
            title: 'Atención',
            text: 'La contraseña no puede estar vacía',
        });
        return;
    }

    $.ajax({
        url: URL_CHANGE_PASSWORD.replace("0", userId),
        method: 'POST',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            password: newPassword
        },
        success: function(response) {
            Swal.fire({
                icon: 'success',
                title: 'Éxito',
                text: 'Contraseña cambiada con éxito',
            }).then(() => {
                $('#passwordModal').modal('hide'); // Cerrar el modal
                $('#newPassword').val(''); // Limpiar el campo de contraseña
            });
        },
        error: function(error) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Hubo un problema al cambiar la contraseña',
            });
        }
    });
}

