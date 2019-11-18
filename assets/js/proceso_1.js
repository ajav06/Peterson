var termine = false;

self.addEventListener('message', function (event) {
    termine = true;
});

function proceso1(){
    var contador = 0;
    do {
        self.postMessage('flag');
        self.postMessage('turno');
        console.log(termine);
        if (termine==false){
            console.log("no he terminado");
            setTimeout(proceso1,1000);
        } else {
            console.log("Proceso 1: Sección crítica");
            cscVar++;
            console.log(cscVar);
            contador++;
            console.log("Contador es: " + contador.toString());
            flag[i] = false;
        }
    } while (contador < 5);    
}

proceso1();