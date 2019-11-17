do {
    self.postMessage('ola')
    flag[j] = true;
    turno = i;
    while (flag[i] && turno == i);
    console.log("Proceso 2: Sección crítica");
    cscVar--;
    console.log(cscVar);
    contador++;
    console.log("Contador es: " + contador.toString());
    flag[j] = false;
} while (contador < 5);