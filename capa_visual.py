def perdiste():
    """Imprime perdiste"""
    print("Perdiste")

def ganaste():
    """Imprime ganaste"""
    print("Ganaste")

def movimientos_validos():
    """Imprime los movimientos validos"""
    print("Los movimientos son: \n W = arriba \n S = abajo \n A = izquierda \n D = derecha\n")

def gracias():
    """Imprime un agradecimiento por jugar"""
    print("Gracias por jugar :)")

def imprimir_matriz(matriz):
    """Imprime el tablero"""
    fila = ""
    for l in range(len(matriz)):
        for l2 in range(len(matriz[l])):
            fila += matriz[l][l2] + "   "
        print(fila)
        fila = "" #Hace que no se acumulen las filas
        print("")