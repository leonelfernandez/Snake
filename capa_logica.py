import random
from capa_visual import imprimir_matriz
CANT_FILAS = 5
CANT_COLUMNAS = 7
TAMAÑO_FINAL_SERPIENTE = 7

def actualizar_tablero():
	"""Esta funcion me define el tamaño del entorno donde se va a mover la serpiente"""
	tablero = []
	for l in range(CANT_FILAS):
		tablero.append([])
		for l2 in range(CANT_COLUMNAS):
			tablero[l].append(".")
	return tablero

def imprimir_tablero(tablero):
	"""Imprime el tablero"""
	imprimir_matriz(tablero)


def actualizar_serpiente(tablero, posiciones_serpiente):
	"""Esta funcion determina la posicion y tamaño inicial de la serpiente"""
	if not me_comi_la_pared(posiciones_serpiente):
		for posicion_serpiente in posiciones_serpiente:
			tablero[posicion_serpiente[0]][posicion_serpiente[1]] = "#"

def actualizar_fruta(tablero,posicion_fruta):
	"""Coloca frutas en el tablero de forma aleatoria"""
	tablero[posicion_fruta[0]][posicion_fruta[1]] = "*"

def inicializar_fruta(posiciones_serpiente):
	"""Coloca frutas en el tablero de forma aleatoria"""
	lista_de_serpiente = []
	valor_1 = random.randint(0, CANT_FILAS - 1)
	valor_2 = random.randint(0, CANT_COLUMNAS - 1)
	for pos in range(len(posiciones_serpiente)):
		lista_de_serpiente.append((posiciones_serpiente[pos][0], posiciones_serpiente[pos][1]))
	while (valor_1, valor_2) in lista_de_serpiente:
		valor_1 = random.randint(0, CANT_FILAS - 1)
		valor_2 = random.randint(0, CANT_COLUMNAS - 1)
	return valor_1, valor_2

def mover_serpiente(posicion_fruta, direccion, posiciones_serpiente):
	"""Mueve la serpiente segun la accion del usuario"""
	hay_fruta = False
	cabeza = posiciones_serpiente[0]
	posicion_nueva = None

	if (direccion == "arriba" and cabeza[2] != "abajo") \
		or ((direccion == "" or direccion == "abajo") and cabeza[2] == "arriba"):
		posicion_nueva = (cabeza[0]-1, cabeza[1], "arriba")
		posiciones_serpiente.insert(0, posicion_nueva)

	if (direccion == "abajo" and cabeza[2] != "arriba") \
		or ((direccion == "" or direccion == "arriba") and cabeza[2] == "abajo"):
		posicion_nueva = (cabeza[0] + 1, cabeza[1], "abajo")
		posiciones_serpiente.insert(0, posicion_nueva)

	if (direccion == "izquierda" and cabeza[2] != "derecha") \
		or ((direccion == "" or direccion == "derecha") and cabeza[2] == "izquierda"):
		posicion_nueva = (cabeza[0], cabeza[1] - 1, "izquierda")
		posiciones_serpiente.insert(0, posicion_nueva)

	if (direccion == "derecha" and cabeza[2] != "izquierda") \
		or ((direccion == "" or direccion == "izquierda") and cabeza[2] == "derecha"):
		posicion_nueva = (cabeza[0], cabeza[1] + 1, "derecha")
		posiciones_serpiente.insert(0, posicion_nueva)

	if not posicion_fruta == (posicion_nueva[0], posicion_nueva[1]):
		posiciones_serpiente.pop()
	else:
		hay_fruta = True
	return hay_fruta
def me_comi_la_pared(posiciones_serpiente):
	"""Devuelve True si se comio la pared"""
	cabeza = posiciones_serpiente[0]
	return cabeza[0] < 0 or cabeza[1] < 0 or cabeza[0] > CANT_FILAS-1 or cabeza[1] > CANT_COLUMNAS-1

def me_comi_el_cuerpo(posiciones_serpiente):
	"""Devuelve True si se comio el cuerpo"""
	cuerpo = False
	cabeza = posiciones_serpiente[0]
	for i in range(1, len(posiciones_serpiente)):
		if (cabeza[0], cabeza[1]) == (posiciones_serpiente[i][0], posiciones_serpiente[i][1]):
			cuerpo = True
	return cuerpo