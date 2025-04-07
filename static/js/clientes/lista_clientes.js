let tabla_clientes = $('#clientes').DataTable({
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
        {data: 'nombre', title: 'Nombre'},
        {data: 'alias', title: 'Alias'},

    ]
});
