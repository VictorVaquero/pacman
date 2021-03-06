
import numpy as np
import random
import pacman as p
import tablaEstados as t
import copy


CONTADOR = 100
PERCENTAJE = 0.6
TABLERO_ELEGIDO = p.tablero_ultrapequeño


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


def politica(jugador, fantasmas, tablero, tabla, percentaje):
    """ Devuelme el movimiento del jugador
        La politica puede ser aleatoria, a trabes de la tabla_q,
        con heuristicas....
    """
    try:
        movimientos = [tabla.get(jugador, fantasmas, tablero, i)
                       for i in range(1, 5)]

        m = movimientos.index(max(movimientos)) + 1
        s = np.random.binomial(1, percentaje)
        if s:
            m = np.random.randint(1, 5)
    except KeyError:
        m = np.random.randint(1, 5)
    return (m)


pac = p.Pacman(TABLERO_ELEGIDO)
# tabla_q = t.tablaEstados("Bruto")
(x, y) = TABLERO_ELEGIDO.shape
tabla_q = t.tablaEstados("Red", [x * y, 1], "rectified")


while CONTADOR != 0:
    # print(pac.imprimir())

    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = copy.deepcopy(pac.tablero)

    m = politica(jugador, fantasmas, tablero, tabla_q, PERCENTAJE)
    premio = pac.actualizar(m)

    tabla_q.update(jugador, fantasmas, tablero, m, premio)

    if(pac.aGanado() or pac.aPerdido()):
        print("Prueba %i, puntuacion %i", CONTADOR, pac.puntuacion)
        pac.reset()
        CONTADOR -= 1


# Probamos ahora la Politica


# Interfaz fisica
# Politica es una funcion, le puedes pasar mov()
# u otra funcion cualquiera
PARTIDAS = 5
print(pac.imprimir())
while PARTIDAS != 0:
    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = copy.deepcopy(pac.tablero)
    pac.actualizar(politica(jugador, fantasmas, tablero, tabla_q, 0))
    print(pac.imprimir())
    if(pac.aGanado() or pac.aPerdido()):
        print("Partida %i, puntuacion %i", PARTIDAS,
              pac.puntuacion, pac.aGanado())
        pac.reset()
        PARTIDAS -= 1
