import random
from capa_visual import imprimir_matriz, imprimir_nivel
from capa_archivos import lectura, lectura_csv
def inicializar_mochila():
	"""Obtiene la mochila"""
	especiales = []
	especiales_csv = lectura_csv("especiales.csv")
	for especial_csv in especiales_csv: 
		#La (simbolo, tecla, cantidad, descripcion, atributo, valor) 
		especial = (especial_csv[0],especial_csv[3], 0, especial_csv[4], especial_csv[1], especial_csv[2])
		especiales.append(especial)
	return especiales
def actualizar_mochila(MOCHILA, simbolo):
	"""Actualiza la cantidad de especiales que tenes en la mochila"""
	tupla_especial = ()
	indice_tupla_especial = 0
	for i in range(len(MOCHILA)):
		if MOCHILA[i][0] == simbolo:
			tupla_especial = MOCHILA[i]
			indice_tupla_especial = i
	tupla_especial = (tupla_especial[0], tupla_especial[1], tupla_especial[2]+1, tupla_especial[3], tupla_especial[4], tupla_especial[5])
	MOCHILA[indice_tupla_especial] = tupla_especial
	return MOCHILA			

def ejecutar_especial(poder_especial, ESPECIALES, dif_velocidad, dif_tamaño, MOCHILA): # "$"(T+1) "%"(VEL) "&"(T-1)
	"""Ejecuta el poder especial presionado, que fue asignado por tecla"""
	tupla_especial = ()
	indice_tupla_especial = 0
	for i in range(len(MOCHILA)):
		if MOCHILA[i][0] == poder_especial and MOCHILA[i][2] >= 1:
			tupla_especial = MOCHILA[i]
			indice_tupla_especial = i
			if tupla_especial[4] == "VELOCIDAD":
				dif_velocidad += float(tupla_especial[5])
			elif tupla_especial[4] == "LARGO":
				dif_tamaño += int(tupla_especial[5])
	if not tupla_especial == ():
		tupla_especial = (tupla_especial[0], tupla_especial[1], tupla_especial[2]-1, tupla_especial[3], tupla_especial[4], tupla_especial[5])
		MOCHILA[indice_tupla_especial] = tupla_especial
	return dif_velocidad, dif_tamaño, MOCHILA	


def asignacion_niveles(NIVEL_ACTUAL, TAMAÑO_FINAL_SERPIENTE, velocidad, CANT_COLUMNAS, CANT_FILAS, ESPECIALES, dif_tamaño):
	"""Recibe la ruta y asigna el nivel recibido"""
	velocidad = 0
	dif_tamaño = 0
	elementos_nivel = lectura("nivel_" + str(NIVEL_ACTUAL) + ".txt")
	TAMAÑO_FINAL_SERPIENTE = int(elementos_nivel[0])
	velocidad = float(elementos_nivel[1])
	dimensiones = elementos_nivel[2].split("x")
	CANT_FILAS, CANT_COLUMNAS = int(dimensiones[0]), int(dimensiones[1])
	obstaculos = elementos_nivel[3].split(";")
	POSICION_OBSTACULOS = []
	for obstaculo in obstaculos:
		coordenada = obstaculo.split(",")
		POSICION_OBSTACULOS.append((int(coordenada[0]), int(coordenada[1])))
	ESPECIALES = elementos_nivel[4].split(",")
	return TAMAÑO_FINAL_SERPIENTE, velocidad, CANT_COLUMNAS, CANT_FILAS, ESPECIALES, POSICION_OBSTACULOS, dif_tamaño
	
def actualizar_tablero(CANT_FILAS, CANT_COLUMNAS):
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

def actualizar_obstaculos(tablero, POSICION_OBSTACULOS):
	"""Esta funcion determina la posicion de los obstaculos"""
	for posicion_obstaculo in POSICION_OBSTACULOS:
			tablero[posicion_obstaculo[0]][posicion_obstaculo[1]] = "@"

def inicializar_especiales(ESPECIALES, CANT_FILAS, CANT_COLUMNAS, posiciones_serpiente, POSICION_OBSTACULOS, posicion_fruta, tablero):
	"""Elije aleatoriamente los especiales y los coloca en una posicion random"""
	simbolo_indice = random.randint(0, len(ESPECIALES) - 1)
	simbolo = ESPECIALES[simbolo_indice]
	lista_de_serpiente = []
	valor_1 = random.randint(0, CANT_FILAS - 1)
	valor_2 = random.randint(0, CANT_COLUMNAS - 1)
	for pos in range(len(posiciones_serpiente)):
		lista_de_serpiente.append((posiciones_serpiente[pos][0], posiciones_serpiente[pos][1]))
	while (valor_1, valor_2) in lista_de_serpiente or (valor_1, valor_2) in POSICION_OBSTACULOS or (valor_1, valor_2) == posicion_fruta:
		valor_1 = random.randint(0, CANT_FILAS - 1)
		valor_2 = random.randint(0, CANT_COLUMNAS - 1)
	
	return valor_1, valor_2, simbolo

def actualizar_especial(tablero, posicion_especial,simbolo):
	"""Coloca especiales en el tablero de forma aleatoria"""
	tablero[posicion_especial[0]][posicion_especial[1]] = simbolo
	return tablero

def inicializar_serpiente():
	"""Retorna el valor inicial de la serpiente"""
	return [(0, 0, "abajo")]

def actualizar_serpiente(tablero, posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS):
	"""Esta funcion determina la posicion y tamaño inicial de la serpiente"""
	if not me_comi_la_pared(posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS):
		for posicion_serpiente in posiciones_serpiente:
			tablero[posicion_serpiente[0]][posicion_serpiente[1]] = "#"

def actualizar_fruta(tablero,posicion_fruta):
	"""Coloca frutas en el tablero de forma aleatoria"""
	tablero[posicion_fruta[0]][posicion_fruta[1]] = "*"

def inicializar_fruta(posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS, POSICION_OBSTACULOS, posicion_especial):
	"""Coloca frutas en el tablero de forma aleatoria"""
	lista_de_serpiente = []
	valor_1 = random.randint(0, CANT_FILAS - 1)
	valor_2 = random.randint(0, CANT_COLUMNAS - 1)
	for pos in range(len(posiciones_serpiente)):
		lista_de_serpiente.append((posiciones_serpiente[pos][0], posiciones_serpiente[pos][1]))
	while (valor_1, valor_2) in lista_de_serpiente or (valor_1, valor_2) in POSICION_OBSTACULOS or (valor_1, valor_2) == posicion_especial:
		valor_1 = random.randint(0, CANT_FILAS - 1)
		valor_2 = random.randint(0, CANT_COLUMNAS - 1)
	return valor_1, valor_2

def mover_serpiente(posicion_fruta, direccion, posiciones_serpiente, posicion_especial, dif_tamaño):
	"""Mueve la serpiente segun la accion del usuario"""
	hay_fruta = False
	cabeza = posiciones_serpiente[0]
	posicion_nueva = None
	hay_especial = False
	
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
		if dif_tamaño <= 0:
			posiciones_serpiente.pop()
			while dif_tamaño < 0:
				posiciones_serpiente.pop()
				dif_tamaño += 1
		else:
			dif_tamaño -= 1	
	else:
		hay_fruta = True
	
	if posicion_especial == (posicion_nueva[0], posicion_nueva[1]):
		hay_especial = True
	
	return hay_fruta, hay_especial, dif_tamaño

def me_comi_el_obstaculo(posiciones_serpiente, tablero):
	"""Devuelve True si se comio el obstaculo"""
	cabeza = posiciones_serpiente[0]
	if tablero[cabeza[0]][cabeza[1]] == "@":
		return True
	return False

def me_comi_la_pared(posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS):
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