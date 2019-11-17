var turno;
var flag = [false,false];
var i=0;
var j=1;
var contador=0;
var cscVar=13;

function peterson(){
    console.log("Algoritmo de Peterson");
    var p1 = new Worker("assets/js/proceso_1.js");
    //var p2 = new Worker("assets/js/proceso_2.js");

    p1.addEventListener('message', function(event){
        if(event.data == 'flag'){
            flag[i] = true;
            console.log('cambié flag proceso 1');
        }
        if (event.data == 'turno'){
            turno = j;
            console.log('cambié turno proceso 1');
        }
    }); 

    setTimeout(p1.postMessage('termine'),2000);
    
    //p2.addEventListener('message', function(event){
        //console.log("mensaje recibido del proceso 2");
    //});

}