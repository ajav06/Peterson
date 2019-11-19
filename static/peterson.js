function peterson(){
    $.ajax({
        url: '/_peterson',
        type: 'GET',
        data: {},
        dataType: 'json',
        success: function(data) {
            if (data.critico == 1){
                document.getElementById("critica").innerHTML = "Proceso 1 en sección crítica."
            } else if (data.critico == 2){
                document.getElementById("critica").innerHTML = "Proceso 2 en sección crítica."
            }
        }
    });
}

function comenzar(){
    document.getElementById("critica").innerHTML = "Comenzando Peterson..."
    setInterval(peterson(),5000);
}
