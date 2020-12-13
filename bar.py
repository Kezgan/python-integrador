import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

meseros = 3
barman = 1
barra = []

class Barman(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.name = 'Barman'
        self.monitor = monitor

    def barmanBebidas(self):
        return random.randint(1, 10)

    def dejarBebidas(self):
        bebidasAPoner = self.barmanBebidas()
        with self.monitor:
            for _ in range(bebidasAPoner):
                barra.append(0)
            logging.info(f'Acabo de dejar en la barra {bebidasAPoner}. El total de bebidas en la barra es de {len(barra)}')
            self.monitor.notify()
            time.sleep(4)

    def run(self):
        while(True):
            self.dejarBebidas()

class Mesero(threading.Thread):
    def __init__(self, monitor, numero):
        super().__init__()
        self.name = f'Mesero {numero}'
        self.monitor = monitor

    def meseroBebidas(self):
        return random.randint(1, 10)

    def agarrarBebidas(self):
        bebidasASacar = self.meseroBebidas()
        with self.monitor:
            while len(barra) < bebidasASacar:
                logging.info(f'No hay suficientes bebidas en la barra. Voy a esperar')
                self.monitor.wait()
            for _ in range(bebidasASacar):
                barra.pop(0)
            logging.info(f'Agarré {bebidasASacar} bebidas para entregar a los clientes. En la barra quedaron {len(barra)}')
            time.sleep(4)
    
    def run(self):
        while(True):
            self.agarrarBebidas()


monitor = threading.Condition()

Barman(monitor).start()

for i in range(meseros):
    Mesero(monitor, i).start()