import time
import random
import threading
import sys

N = 5
TIEMPO_TOTAL = 2


class filosofo(threading.Thread):
    semaforo = threading.Lock()  # SEMAFORO BINARIO ASEGURA LA EXCLUSION MUTUA
    estado = []  # PARA CONOCER EL ESTADO DE CADA FILOSOFO
    tenedores = []  # ARRAY DE SEMAFOROS PARA SINCRONIZAR ENTRE FILOSOFOS, MUESTRA QUIEN ESTA EN COLA DEL TENEDOR
    count = 0

    def __init__(self):
        super().__init__()  # HERENCIA
        self.id = filosofo.count  # DESIGNA EL ID AL FILOSOFO
        filosofo.count += 1  # AGREGA UNO A LA CANT DE FILOSOFOS
        # EL FILOSOFO ENTRA A LA MESA EN ESTADO PENSANDO
        filosofo.estado.append('PENSANDO')
        # AGREGA EL SEMAFORO DE SU TENEDOR( TENEDOR A LA IZQUIERDA)
        filosofo.tenedores.append(threading.Semaphore(0))
        print("FILOSOFO {0} - PENSANDO".format(self.id))

    def __del__(self):
        # NECESARIO PARA SABER CUANDO TERMINA EL THREAD
        print("FILOSOFO {0} - Se para de la mesa".format(self.id))

    def pensar(self):
        # CADA FILOSOFO SE TOMA DISTINTO TIEMPO PARA PENSAR, ALEATORIO
        time.sleep(random.randint(0, 5))

    def derecha(self, i):
        return (i-1) % N  # BUSCAMOS EL INDICE DE LA DERECHA

    def izquierda(self, i):
        return(i+N-1) % N  # BUSCAMOS EL INDICE DE LA IZQUIERDA

    def verificar(self, i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i] = 'COMIENDO'
            # SI SUS VECINOS NO ESTAN COMIENDO AUMENTA EL SEMAFORO DEL TENEDOR Y CAMBIA SU ESTADO A COMIENDO
            filosofo.tenedores[i].release()

    def tomar(self):
        filosofo.semaforo.acquire()  # SEÑALA QUE TOMARA LOS TENEDORES (EXCLUSION MUTUA)
        filosofo.estado[self.id] = 'HAMBRIENTO'
        # VERIFICA SUS VECINOS, SI NO PUEDE COMER NO SE BLOQUEARA EN EL SIGUIENTE ACQUIRE
        self.verificar(self.id)
        # SEÑALA QUE YA DEJO DE INTENTAR TOMAR LOS TENEDORES (CAMBIAR EL ARRAY ESTADO)
        filosofo.semaforo.release()
        # SOLO SI PODIA TOMARLOS SE BLOQUEARA CON ESTADO COMIENDO
        filosofo.tenedores[self.id].acquire()

    def soltar(self):
        filosofo.semaforo.acquire()  # SEÑALA QUE SOLTARA LOS TENEDORES
        filosofo.estado[self.id] = 'PENSANDO'
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        filosofo.semaforo.release()  # YA TERMINO DE MANIPULAR TENEDORES

    def comer(self):
        print("FILOSOFO {} COMIENDO".format(self.id))
        time.sleep(random.randint(1, 3))  # TIEMPO ARBITRARIO PARA COMER
        print("FILOSOFO {} TERMINO DE COMER".format(self.id))

    def run(self):
        for i in range(TIEMPO_TOTAL):
            self.pensar()  # EL FILOSOFO PIENSA
            self.tomar()  # AGARRA LOS TENEDORES CORRESPONDIENTES
            self.comer()  # COME
            self.soltar()  # SUELTA LOS TENEDORES


def main():
    lista = []
    for i in range(N):
        lista.append(filosofo())  # AGREGA UN FILOSOFO A LA LISTA

    for f in lista:
        f.start()  # ES EQUIVALENTE A RUN()

    for f in lista:
        f.join()  # BLOQUEA HASTA QUE TERMINA EL THREAD


if __name__ == "__main__":
    main()
