# Creo que el problema que hay es que cuando un mesero se pone en espera en la otra vuelta agarra tragos pero recien al final, y creo que debería ser al principio, ya que al estar esperando deberia
# tener prioridad.

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

    def barmanTragos(self):
        return random.randint(1, 10)

    def dejarTragos(self):
        tragosAPoner = self.barmanTragos()
        with self.monitor:
            logging.info(f'Preparando tragos...')
            time.sleep(1)
            for _ in range(tragosAPoner):
                barra.append(0)
            logging.info(f'Acabo de dejar en la barra {tragosAPoner}. El total de tragos en la barra es de {len(barra)}')
            self.monitor.notify()
            time.sleep(4)

    def run(self):
        while(True):
            self.dejarTragos()

class Mesero(threading.Thread):
    def __init__(self, monitor, numero):
        super().__init__()
        self.name = f'Mesero {numero}'
        self.monitor = monitor

    def meseroTragos(self):
        return random.randint(1, 10)

    def agarrarTragos(self):
        tragosASacar = self.meseroTragos()
        with self.monitor:
            while len(barra) < tragosASacar:
                logging.info(f'No hay suficientes tragos en la barra. Voy a esperar')
                self.monitor.wait()
            for _ in range(tragosASacar):
                barra.pop(0)
            logging.info(f'Agarré {tragosASacar} tragos para entregar a los clientes. En la barra quedaron {len(barra)}')
            time.sleep(4)
    
    def run(self):
        while(True):
            self.agarrarTragos()


monitor = threading.Condition()

Barman(monitor).start()

for i in range(meseros):
    Mesero(monitor, i).start()