import numpy as np
import random


class Pacman:

    # Valores representados en el tablero
    SUELO = 0  # 0 hueco posible
    PARED = 1  # 1 paredes
    PUNTO = 2  # 2 puntos
    GALLETA = 3  # 3 galleta

    # Puntos ganados por punto cogido
    PUNTO_VALOR = 1
    # Puntos por perder partida
    PUNTO_PERDIDA = -10

    # Estado final
    JUGANDO = 0
    CAZADO = 1
    GANADO = 2

    # Diccionario con los movimientos
    # -Y,X
    movimientos = {
        1: (0, -1),
        2: (0, 1),
        3: (-1, 0),
        4: (1, 0)
    }

    # Graficos del juego
    simbolos = {
        0: " ",
        1: "#",
        2: ".",
        3: "o"
    }

    # Funciones de Inicializacion

    def __init__(self, tablero, num_fantasmas=1):
        """ Inicializa el tablero con los agentes
            puntos y galletas
        """
        self.tablero = tablero
        self.num_fantasmas = num_fantasmas
        self.puntuacion = 0
        self.estado = self.JUGANDO

        self.inicializar_jugadores()
        self.inicializar_puntos()

    def inicializar_jugadores(self):
        """ Inicializa el tablero con los agentes,
            1 jugador y f fantasmas, default 1
        """
        s = self.tablero.shape
        t = False
        while(not t):
            x = np.random.randint(s[0])
            y = np.random.randint(s[1])
            if(self.tablero[x, y] == self.SUELO):
                self.jugador = (x, y)
                t = True
        self.fantasmas = []
        for i in range(self.num_fantasmas):
            t = False
            while(not t):
                x = np.random.randint(s[0])
                y = np.random.randint(s[1])
                if(self.tablero[x, y] == self.SUELO and
                        (x, y) != self.jugador):
                    self.fantasmas.append((x, y))
                    t = True

    def inicializar_puntos(self):
        """ Añade puntos al tablero en todos los huecos
            del tablero, una vez añadido el resto
        """
        s = self.tablero.shape
        for i in range(s[0]):
            for j in range(s[1]):
                if (self.tablero[i, j] == self.SUELO and
                        (i, j) != self.jugador):
                    self.tablero[i, j] = self.PUNTO

    # Funciones de actualizacion

    def actualizar(self, movimiento):
        """ Mueve a pacman segun el movimiento
            iz - 1  de - 2  arri - 3  abj -4
            si hay colision no hay movimiento.
            Los fantasmas se mueven aleatoriamente
        """
        mx, my = self.movimientos[movimiento]
        s = self.tablero.shape
        x, y = self.jugador
        puntos = 0

        nx, ny = x + mx, y + my
        if (nx, ny) in self.fantasmas:
            self.estado = self.CAZADO
            puntos += self.PUNTO_PERDIDA
        elif self.tablero[nx, ny] != self.PARED:
            if(self.tablero[nx, ny] == self.PUNTO):
                puntos += self.PUNTO_VALOR
                self.tablero[nx, ny] = self.SUELO
            self.jugador = (nx, ny)

        faux = []
        for fantasma in self.fantasmas:
            move = False
            while not move:
                m = np.random.randint(1, 5)
                mx, my = self.movimientos[m]
                x, y = fantasma

                nx, ny = x + mx, y + my

                if ((nx, ny) not in self.fantasmas and
                        self.tablero[nx, ny] != self.PARED):
                    faux.append((nx, ny))
                    move = True
                    if (nx, ny) == self.jugador:
                        self.estado = self.CAZADO
                        puntos += self.PUNTO_PERDIDA
        self.fantasmas = faux

        fin = True
        for i in range(s[0]):
            for j in range(s[1]):
                if self.tablero[i, j] == self.PUNTO:
                    fin = False
        if fin:
            self.estado = self.GANADO

        self.puntuacion += puntos
        return puntos

    def aGanado(self):
        return self.estado == self.GANADO

    def aPerdido(self):
        return self.estado == self.CAZADO

    def imprimir(self):
        s = self.tablero.shape

        st = ""
        for i in range(s[0]):
            for j in range(s[1]):
                aux = self.simbolos[self.tablero[i, j]]
                if self.jugador == (i, j):
                    aux = "P"
                if (i, j) in self.fantasmas:
                    aux = "F"
                st += aux
            st += "\n"
        return st


        def politica(self,tabla):
            """ A partir de un diccionario, elige el mejor
                movimiento
            """
            fantasmas = tuple(self.fantasmas)
            tablero = tuple(map(tuple, np.asarray(self.tablero)))
            movimientos = {tabla[self.jugador,fantasmas,tablero,i] for i in range(1,5)}
            return np.argmax(movimientos)


mapeo = {
    "w": 3,
    "a": 1,
    "s": 4,
    "d": 2
}


def mov():
    """Movimiento con el teclado
    """
    inp = None
    while inp is None:
        aux = input("Movimiento :")
        try:
            inp = mapeo[aux]
        except KeyError:
            print("Fuck u")
    return inp







# Main shit

# Tablero pequeño
tablero_pequeño = np.matrix("""1 1 1 1 1 1;
                       1 0 0 0 1 1;
                       1 0 1 0 0 1;
                       1 0 1 1 0 1;
                       1 0 0 0 0 1;
                       1 1 1 1 1 1""")

# Tablero grande
tablero_grande = np.matrix("""1 1 1 1 1 1 1 1;
                       1 0 0 0 0 0 0 1;
                       1 0 1 0 0 1 0 1;
                       1 0 1 1 0 1 0 1;
                       1 0 0 0 0 1 0 1;
                       1 1 1 1 0 0 0 1;
                       1 0 0 0 0 0 0 1;
                       1 1 1 1 1 1 1 1""")
