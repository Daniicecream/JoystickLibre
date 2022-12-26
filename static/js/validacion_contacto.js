$(document).ready(function () {
    $("#contact-form").validate({
        rules: {
            nick: {
                required: true,
                minlength: 3
            },
            nombre: {
                required: true,
                minlength: 5
            },
            sexo: {
                required: true
            },
            nacimiento: {
                required: true
            },
            email: {
                required: true,
                email: true
            },
            mensaje: {
                required: true
            },
            TerminosCondiciones: {
                required: true
            }
        },
        messages: {
            nick: {
                required: "(*)Campo Obligatorio",
                minlength: "El nick debe ser de al menos 3 caracteres"
            },
            nombre: {
                required: "(*)Campo Obligatorio",
                minlength: "El nombre al menos debe tener 5 caracteres"
            },
            sexo: {
                required: "(*)Campo Obligatorio"
            },
            nacimiento: {
                required: "(*)Campo Obligatorio",
            },
            email: {
                required: "(*)Campo Obligatorio",
                email: "Ingrese un formato de email valido"
            },
            mensaje: {
                required: "(*)Campo Obligatorio"
            },
            TerminosCondiciones: {
                required: "(*)Campo Obligatorio"
            }
        },
        errorElement: 'span'
    });
});