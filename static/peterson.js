function peterson(){
    $.ajax({
        url: '/_peterson',
        type: 'GET',
        data: {},
        dataType: 'json',
        success: function(data) {
            alert(data.respuesta);
        }
    });
}