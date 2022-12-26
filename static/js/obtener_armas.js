/*const settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://valorant-weapons.p.rapidapi.com/weapon/" + nombre,
    "method": "GET",
    "headers": {
        "x-rapidapi-key": "1c0b9e32f3msh86c5829ce1a0d62p165a76jsn14cdcea87344",
        "x-rapidapi-host": "valorant-weapons.p.rapidapi.com"
    }
};
$.ajax(settings).done(function (response) {
    console.log(response);
});*/

$( document ).ready(function(){
    
    var nombre;
    console.log('variable global nombre creada');

    $('#arma').change((function (event){
        event.preventDefault();  
        nombre = $('#arma').val();
        console.log(nombre+' obtenida del combobox');
    
    }));

    $('#btn-buscar-arma').click(function (event) {
        event.preventDefault();
    
        $.ajax({
            url: 'https://valorant-weapons.p.rapidapi.com/weapon/' + nombre + '/?rapidapi-key=1c0b9e32f3msh86c5829ce1a0d62p165a76jsn14cdcea87344',
            data: {
                format: 'json'
            },
            error: function () {
                $('#info').html('<p> Lo sentimos ha ocurrido un error </p>');
                $("h2").css({'color':'red'});
            },
            dataType: 'json',
            success: function (data) {
                console.log(data);
    
                var $nom_arma = $('<p class="info-titulo fw-300 centrar-texto">').text(data.name);
                var $coste_arma = $('<p class="info-detalle centrar-texto">').text('Coste: '+data.cost);
                var $tipo_disparo = $('<p class="info-detalle centrar-texto">').text('Tipo de tiro: '+data.fire_type);
                var $cadencia_disparo = $('<p class="info-detalle centrar-texto">').text('Cadencia de tiro: '+data.fire_rate);
                var $tiempo_recarga = $('<p class="info-detalle centrar-texto">').text('Tiempo de recarga: '+data.reload_speed);
                var $capacidad = $('<p class="info-detalle centrar-texto">').text('Capacidad: '+data.magazine);
                var $dispersion = $('<img class=img-arma src="'+data.spread+'.png" alt="Imagen que muestra el patron de disperción del arma">');
    
                $("#info").empty();     // para limpiar el contedor antes de desplegar
                $('#info')
                    .append($nom_arma)
                    .append($coste_arma)
                    .append($tipo_disparo)
                    .append($cadencia_disparo)
                    .append($tiempo_recarga)
                    .append($capacidad)
                    .append($dispersion)
                    .append('<br>Referencia de dispersion')

            },
            type: 'GET'
        });

    });


});


