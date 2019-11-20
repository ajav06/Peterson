function peterson(){
    ejecutar();
    $.ajax({
        url: '/_peterson',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            if (data.proceso_critico != proceso_critico){
                cambiar_chofer(data.proceso_critico);
            }
        }
    });
    setTimeout(function(){
        setInterval(chequeo_chofer,6500)
    },);
}
