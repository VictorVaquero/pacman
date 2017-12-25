
import numpy as np
import random
import pac as p

ALFA = 0.1
DISCOUNT = 0.9
CONTADOR = 100






def politica():
    """ Devuelme el movimiento del jugador
        La politica puede ser aleatoria, a trabes de la tabla_q,
        con heuristicas....
    """
    m = np.random.randint(1, 4)
    return (m)




def futuro_premio(pac, tabla_q):
    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = tuple(map(tuple, np.asarray(pac.tablero)))

    # TODO Hacerlo con una comprension listas
    premio = None
    for i in range(1, 5):
        aux = tabla_q[jugador, fantasmas, tablero, i]
        if(premio is None or premio < aux)
            premio = aux













pac = p.pac(p.tablero_pequeño)

# Diccionario con todos los estados, tuplas van
# (jugador,fantasmas,tablero,movimiento) : Premio esperado
tabla_q = {}

while CONTADOR != 0:
    m = politica()
    jugador = pac.jugador
    fantasmas = tuple(pac.fantasmas)
    tablero = tuple(map(tuple, np.asarray(pac.tablero)))
    premio = pac.actualizar(m)

    tabla_q[jugador, fantasmas, tablero, m] =           \
        (1 - ALFA) * tabla_q[jugador, fantasmas, tablero, m] + \
        ALFA * (premio + DISCOUNT*futuro_premio(pac,tabla_q))
    CONTADOR -= 1


# Probamos ahora la Politica


# Interfaz fisica
# Politica es una funcion, le puedes pasar mov()
# u otra funcion cualquiera

print(pac.imprimir())
while True:
    pac.actualizar(pac.politica(tabla_q))
    print(pac.imprimir())
    print(pac.puntuacion)
    if(pac.aGanado() or pac.aPerdido()):
        break

print("Has tenido %i puntos", pac.puntuacion)
if pac.aGanado():
    print("Enorabuena")
if(pac.aPerdido()):
    print("Jodete")
