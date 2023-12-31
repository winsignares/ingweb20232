if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var latitud = position.coords.latitude;
        var longitud = position.coords.longitude;

        alert(latitud)

       /* // Mostrar la latitud y longitud en la página
        document.getElementById("latitud").textContent = latitud;
        document.getElementById("longitud").textContent = longitud;
*/
        // Crear un objeto con los datos a enviar en formato JSON
        var data = {
            idcliente: 1,
            latitud: latitud,
            longitud: longitud
        };

        // Configurar encabezados para enviar JSON
        var config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };

        // Realizar una solicitud POST a la API en Python
        axios.post('api/saveruta', JSON.stringify(data), config)
            .then(function (response) {
                console.log('Datos enviados con éxito:', response.data);
            })
            .catch(function (error) {
                console.error('Error al enviar datos:', error);
            });
    });
} else {
    console.log("El navegador no admite la geolocalización.");
}

function saludar() {
    let nombre= document.getElementById('namecliente').value

    alert(nombre)
    
}

function savecliente(){
    let var_nombre= document.getElementById('namecliente');
    
    var data = {
        nombre: var_nombre.value
    };

    var config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    let ruta= 'api/savecliente'

    // Realizar una solicitud POST a la API en Python
    axios.post(ruta, JSON.stringify(data), config)
    .then(function (response) {
        var_nombre.value="";
        console.log('respuesta del backend:', response.data);
        alertify.alert(response.data, function(){
    alertify.message(response.data);
  });
    })
    .catch(function (error) {
        console.error('Error al enviar datos:', error);
    });

}