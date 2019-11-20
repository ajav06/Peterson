var chofer = "Elizabeth";
var copiloto = "Mar";
var imgchofer = "/static/elizabeth.jpg";
var imgcopiloto = "/static/mar.jpg";
var proceso_critico = "1";

function ejecutar() {
    $("#caja").css("display", "");
    $("#encabezado").css("display", "none");
    document.getElementById("algoritmo").innerHTML = "El algoritmo de Peterson de exclusión mutua funciona para que " +
        "dos procesos se ejecuten en concurrencia, compartiendo recursos entre sí.";
    setTimeout(function () {
        document.getElementById("algoritmo").innerHTML = "En este caso, veremos dos choferes manejar un mismo automóvil de forma concurrente.";
        setTimeout(function () {
            document.getElementById("algoritmo").innerHTML = "<img src=\"/static/tesla.jpg\" style=\"width:20%\">" +
                "<div class=\"columns\" style=\"margin-top:20px;\">" + 
                    "<div class=\"column\">" +
                        "<div class=\"title\">Chofer: </div>"+
                        "<div class=\"subtitle\" id=\"chofer-nombre\">Elizabeth</div>"+
                        "<img src=\"/static/elizabeth.jpg\" id=\"chofer-foto\" style=\"width:40%\">" + 
                        "<div class=\"notification is-success\" id=\"estatus-chofer\" style=\"display:none\">"+
                            "Estoy cansada de manejar. ¿Manejas tú?"+
                        "</div>"+
                    "</div>" + 
                    "<div class=\"column\">" +
                       "<div class=\"title\">Copiloto: </div>"+
                        "<div class=\"subtitle\" id=\"copiloto-nombre\">Mar</div>"+
                        "<div class=\"notification is-primary\" id=\"estatus-copiloto\" style=\"display:none\">"+
                            "Por supuesto. Déjame prepararme..."+
                        "</div>"+
                        "<img src=\"/static/mar.jpg\" id=\"copiloto-foto\" style=\"width:40%\">" + 
                    "</div>" + 
                "</div>";
                setInterval(cambio_chofer,20000);
        },2500);
    }, 4000);
}

function cambio_chofer(){
    $("#estatus-chofer").css("display","");
    setTimeout(function(){
        $("#estatus-copiloto").css("display","");
        setTimeout(function(){
            $("#estatus-chofer").css("display","none");
            document.getElementById("estatus-copiloto").innerHTML = "Ya estoy lista. Vamos a cambiar.";
            setTimeout(function(){
                document.getElementById("chofer-nombre").innerHTML = copiloto;
                document.getElementById("copiloto-nombre").innerHTML = chofer;
                $("#chofer-foto").attr("src",imgcopiloto);
                $("#copiloto-foto").attr("src",imgchofer);
                $("#estatus-copiloto").css("display","none");
                document.getElementById("estatus-chofer").innerHTML = "Listo, descansa un rato.";
                $("#estatus-chofer").css("display","");
                setTimeout(function(){
                    document.getElementById("estatus-copiloto").innerHTML = "Mucho mejor, ¡gracias!";
                    $("#estatus-copiloto").css("display","");
                    var aux = chofer;
                    var imgaux = imgchofer;
                    chofer = copiloto;
                    imgchofer = imgcopiloto;
                    copiloto = aux;
                    imgcopiloto = imgaux;
                    setTimeout(function(){
                        $("#estatus-chofer").css("display","none");
                        $("#estatus-copiloto").css("display","none");
                        document.getElementById("estatus-chofer").innerHTML = "Estoy cansada de manejar. ¿Manejas tú?";
                        document.getElementById("estatus-copiloto").innerHTML = "Por supuesto. Déjame prepararme...";
                    },3000);
                },2500);
            },2500);
        },4000);
    },3000);
}

function chequeo_chofer(){
    $.ajax({
        url: '/check_chofer',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            if (data.proceso_critico != proceso_critico){
                cambiar_chofer(data.proceso_critico);
            }
        }
    });
    console.log("Chofer actual: " + chofer);
    console.log("En espera para manejar: " + copiloto);
}

function cambiar_chofer(chofer){
    
}