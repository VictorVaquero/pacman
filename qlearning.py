
import numpy as np
import random
import pacman as p

ALFA = 0.1
DISCOUNT = 0.9
pac = p.Pacman(p.tablero_pequeño)

# Diccionario con todos los estados, tuplas van
# (jugador,fantasmas,tablero,movimiento) : Premio esperado
tabla_q = {}
while True:
    m = politica()
    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = tuple(map(tuple, np.asarray(pac.tablero)))
    premio = pac.actualizar(m)

    tabla_q[jugador, fantasmas, tablero, m] =           \
        (1 - ALFA) * tabla_q[jugador, fantasmas, tablero, m] + \
        ALFA * (premio + DISCOUNT)


def politica():
    """ Devuelme el movimiento del jugador
        La politica puede ser aleatoria, a trabes de la tabla_q,
        con heuristicas....
    """
    m = np.random.randint(1, 4)
    return (m)


def futuro_premio(pacman, tabla_q):
    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = tuple(map(tuple, np.asarray(pac.tablero)))

    premio = None
    for i in range(1, 5):
        if(premio is None or)
