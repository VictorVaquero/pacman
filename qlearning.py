
import numpy as np
import random
import pacman as p

ALFA = 0.1
DISCOUNT = 0.9
CONTADOR = 10000
TABLERO_ELEGIDO = p.tablero_ultrapequeño





def politica(jugador, fantasmas, tablero,tabla):
    """ Devuelme el movimiento del jugador
        La politica puede ser aleatoria, a trabes de la tabla_q,
        con heuristicas....
    """

    try:
        movimientos = [tabla[jugador,fantasmas,tablero,i] for i in range(1,5)]
        m = movimientos.index(max(movimientos))+1
    except KeyError:
        m = np.random.randint(1, 5)
    return (m)




def futuro_premio(pac, tabla_q):
    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = tuple(map(tuple, np.asarray(pac.tablero)))

    # TODO Hacerlo con una comprension listas
    premio = None
    for i in range(1, 5):
        aux = tabla_q.get((jugador, fantasmas, tablero, i),default)
        if(premio is None or premio < aux):
            premio = aux
    return premio




pac = p.Pacman(TABLERO_ELEGIDO)

# Diccionario con todos los estados, tuplas van
# (jugador,fantasmas,tablero,movimiento) : Premio esperado
tabla_q = {}
default = 0

while CONTADOR != 0:
    #print(pac.imprimir())

    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = tuple(map(tuple, np.asarray(pac.tablero)))
    m = politica(jugador, fantasmas, tablero,tabla_q)
    premio = pac.actualizar(m)

    tabla_q[jugador, fantasmas, tablero, m] =           \
        (1 - ALFA) * tabla_q.get((jugador, fantasmas, tablero, m),default) + \
        ALFA * (premio + DISCOUNT*futuro_premio(pac,tabla_q))

    if(pac.aGanado() or pac.aPerdido()):
        print("Prueba %i, puntuacion %i",CONTADOR, pac.puntuacion)
        pac.reset()
        CONTADOR -= 1


# Probamos ahora la Politica


# Interfaz fisica
# Politica es una funcion, le puedes pasar mov()
# u otra funcion cualquiera
PARTIDAS = 5
print(pac.imprimir())
while PARTIDAS != 0:
    pac.actualizar(pac.politica(tabla_q))
    print(pac.imprimir())
    if(pac.aGanado() or pac.aPerdido()):
        print("Partida %i, puntuacion %i",PARTIDAS, pac.puntuacion, pac.aGanado())
        pac.reset()
        PARTIDAS -= 1
