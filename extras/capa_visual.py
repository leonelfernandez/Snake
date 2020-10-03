
def perdiste():
    """Imprime perdiste"""
    print("Perdiste")

def ganaste():
    """Imprime ganaste"""
    print("¡Felicidades, has superado el juego!")

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

def imprimir_nivel(nivel):
    """Imprime el nivel que esta atravesando el usuario"""
    print(f"Nivel:{nivel}")

def imprimir_mochila(tuplas):
    """Imprime la mochila que contiene los especiales"""
    print("SIMBOLO\t||TECLA\t||CANTIDAD\t||DESCRIPCION")
    for tupla in tuplas:
        print(f"{tupla[0]}\t||{tupla[1]}\t||{tupla[2]}\t\t||{tupla[3]}")
   
