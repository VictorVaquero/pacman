import numpy as np

class tablaEstados:

    DEFAULT = 0


    def brute_set(self,jugador, fantasma, tablero, movimiento,value):
            self.tabla[(jugador,fantasma,tablero,movimiento)] = value


    def brute_get(self,jugador, fantasma, tablero, movimiento):
            return self.tabla.get((jugador,fantasma,tablero,movimiento),self.DEFAULT)




    def __init__(self,metodo):
        self.metodos_set = dict(
            Bruto = self.brute_set,

        )
        self.metodos_get = dict(
            Bruto = self.brute_get,
            
        )

        self.metodo = metodo

        if metodo == "Bruto":
            # Diccionario con todos los estados, tuplas van
            # (jugador,fantasmas,tablero,movimiento) : Premio esperado
            self.tabla = {}

    def get(self,jugador, fantasma, tablero, movimiento):
        return self.metodos_get[self.metodo](jugador, fantasma, tablero, movimiento)

    def set(self,jugador, fantasma, tablero, movimiento,value):
        self.metodos_set[self.metodo](jugador, fantasma, tablero, movimiento,value)
