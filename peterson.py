import threading
import random
import time

class Peterson():
    cancelar = False
    proceso1_desea_entrar = False
    proceso2_desea_entrar = False
    proceso_favorecido = 2

    def seccion_critica_1(self):
        print('\nComenzó sección crítica proceso 1.')
        time.sleep(2)
        print('\nTerminó sección crítica proceso 1.')

    def seccion_critica_2(self):
        print('\nComenzó sección crítica proceso 2.')
        time.sleep(2)
        print('\nTerminó sección crítica proceso 2.')

    def proceso1(self):
        while not self.cancelar:
            self.proceso1_desea_entrar = True
            self.proceso_favorecido = 2

            while self.proceso2_desea_entrar and self.proceso_favorecido == 2 and not self.cancelar:
                pass

            if self.cancelar:
                return
            
            self.seccion_critica_1()

            self.proceso1_desea_entrar = False

        print('\nCerrando el proceso 1.')

    def proceso2(self):
        while not self.cancelar:
            self.proceso_2_desea_entrar = True
            self.proceso_favorecido = 1

            while self.proceso1_desea_entrar and self.proceso_favorecido == 1 and not self.cancelar:
                pass

            if self.cancelar:
                return

            self.seccion_critica_2()

            self.proceso_2_desea_entrar = False

        print('\nCerrando el proceso 2.')

    def main(self): 
        t1 = threading.Thread(target=self.proceso1)
        t2 = threading.Thread(target=self.proceso2)

        t1.start()
        t2.start()

        time.sleep(20)

        self.cancelar = True

if __name__ == "__main__":
    p = Peterson()
    p.main()
