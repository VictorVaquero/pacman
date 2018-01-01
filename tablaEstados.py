import numpy as np
import RedNeuronal as r
import copy


class tablaEstados:

    DEFAULT = 0
    ALFA = 0.4  # Cuanto valoras la informacion pasada
    ETA = 100  # Valor para actualizar la red
    DISCOUNT = 0.9  # Cuanto pierde valor los premios con el tiempo

    def brute_set(self, jugador, fantasmas, tablero, movimiento, value):
        tablero = tuple(map(tuple, np.asarray(tablero)))
        self.tabla[(jugador, fantasmas, tablero, movimiento)] = value

    def brute_get(self, jugador, fantasmas, tablero, movimiento):
        tablero = tuple(map(tuple, np.asarray(tablero)))
        return self.tabla.get((jugador, fantasmas, tablero, movimiento),
                              self.DEFAULT)

    def red_set(self, jugador, fantasmas, tablero, movimiento, value):
        lista = self.combinar(jugador, fantasmas, tablero)
        self.tabla.update(((lista, value),), self.ETA)

    def red_get(self, jugador, fantasmas, tablero, movimiento):
        lista = self.combinar(jugador, fantasmas, tablero)
        return self.tabla.feedforward(lista)

    def combinar(self, jugador, fantasmas, tablero):
        tablero = copy.deepcopy(tablero)
        (tx, ty) = tablero.shape
        tablero[jugador] = 4  # Codificamos para la red
        for f in fantasmas:
            tablero[f] = 5  # Codificamos
        tablero.shape = (tx * ty, 1)

        return tablero

    def __init__(self, metodo, size=None, funcion=None):
        self.metodos_set = dict(
            Bruto=self.brute_set,
            Red=self.red_set,
        )
        self.metodos_get = dict(
            Bruto=self.brute_get,
            Red=self.red_get,
        )

        self.metodo = metodo

        if metodo == "Bruto":
            # Diccionario con todos los estados, tuplas van
            # (jugador,fantasmas,tablero,movimiento) : Premio esperado
            self.tabla = {}
        elif metodo == "Red":
            self.tabla = r.Red(size, funcion)

    def get(self, jugador, fantasmas, tablero, movimiento):
        return self.metodos_get[self.metodo](jugador, fantasmas,
                                             tablero, movimiento)

    def set(self, jugador, fantasmas, tablero, movimiento, value):
        self.metodos_set[self.metodo](
            jugador, fantasmas, tablero, movimiento, value)

    def update(self, jugador, fantasmas, tablero, movimiento, premio):
        new_value = (1 - self.ALFA) * self.get(jugador, fantasmas, tablero, movimiento) + \
            self.ALFA * (premio + self.DISCOUNT *
                         self.predice(jugador, fantasmas, tablero, movimiento))
        self.set(jugador, fantasmas, tablero, movimiento, new_value)
        self.tabla.printf()

    def predice(self, jugador, fantasmas, tablero, movimiento):
        # TODO Hacerlo con una comprension listas
        premio = None
        for i in range(1, 5):
            aux = self.get(jugador, fantasmas, tablero, i)
            if(premio is None or premio < aux):
                premio = aux
        return premio
