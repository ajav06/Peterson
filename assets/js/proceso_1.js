var termine = false;

self.addEventListener('message', function (event) {
    termine = true;
});

do {
    self.postMessage('flag');
    self.postMessage('turno');
    setTimeout(function(){while (!termine){}},1000);
    console.log("Proceso 1: Sección crítica");
    cscVar++;
    console.log(cscVar);
    contador++;
    console.log("Contador es: " + contador.toString());
    flag[i] = false;
} while (contador < 5);

