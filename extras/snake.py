from terminal import timed_input
from terminal import clear_terminal
from capa_visual import *
from capa_logica import *
from capa_interaccion_usuario import *
def main():
	"""Llama a todas las funciones, para asi correr el juego"""
	ESPECIALES = []
	POSICION_OBSTACULOS = []	
	velocidad = 0
	CANT_FILAS = 0
	CANT_COLUMNAS = 0
	TAMAÑO_FINAL_SERPIENTE = 0
	NIVEL_ACTUAL = 1
	MOCHILA = []
	posicion_fruta = None
	dif_tamaño = 0
	dif_velocidad = 0
	
	TAMAÑO_FINAL_SERPIENTE, velocidad, CANT_COLUMNAS, CANT_FILAS, ESPECIALES, POSICION_OBSTACULOS, dif_tamaño = asignacion_niveles(NIVEL_ACTUAL,TAMAÑO_FINAL_SERPIENTE,velocidad, CANT_COLUMNAS, CANT_FILAS, ESPECIALES, dif_tamaño)
	posiciones_serpiente = inicializar_serpiente()
	tablero = actualizar_tablero(CANT_FILAS, CANT_COLUMNAS)
	valor_1, valor_2, simbolo = inicializar_especiales(ESPECIALES, CANT_FILAS, CANT_COLUMNAS, posiciones_serpiente, POSICION_OBSTACULOS, posicion_fruta, tablero)
	posicion_especial = (valor_1, valor_2)
	posicion_fruta = inicializar_fruta(posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS, POSICION_OBSTACULOS, posicion_especial)
	MOCHILA = inicializar_mochila()
	actualizar_obstaculos(tablero, POSICION_OBSTACULOS)
	tablero = actualizar_especial(tablero, posicion_especial, simbolo)
	actualizar_serpiente(tablero, posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS)
	imprimir_tablero(tablero)

	while True:
		direccion, poder_especial = obtener_direccion(velocidad, dif_velocidad)
		dif_velocidad, dif_tamaño, MOCHILA = ejecutar_especial(poder_especial, ESPECIALES, dif_velocidad, dif_tamaño, MOCHILA)
		hay_fruta, hay_especial, dif_tamaño = mover_serpiente(posicion_fruta, direccion, posiciones_serpiente, posicion_especial, dif_tamaño)
		if hay_fruta:
			posicion_fruta = inicializar_fruta(posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS, POSICION_OBSTACULOS, posicion_especial)
		if me_comi_el_cuerpo(posiciones_serpiente) or me_comi_la_pared(posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS) or me_comi_el_obstaculo(posiciones_serpiente, tablero):
			perdiste()
			break
		if len(posiciones_serpiente) == TAMAÑO_FINAL_SERPIENTE:
			ganaste()
			posiciones_serpiente = inicializar_serpiente()
			NIVEL_ACTUAL += 1
			if NIVEL_ACTUAL > 2:
				break
			TAMAÑO_FINAL_SERPIENTE, velocidad, CANT_COLUMNAS, CANT_FILAS, ESPECIALES, POSICION_OBSTACULOS, dif_tamaño = asignacion_niveles(NIVEL_ACTUAL, TAMAÑO_FINAL_SERPIENTE, velocidad, CANT_COLUMNAS, CANT_FILAS, ESPECIALES, dif_tamaño)
			MOCHILA = inicializar_mochila()
		if hay_especial:
			MOCHILA = actualizar_mochila(MOCHILA, simbolo)
			valor_1, valor_2, simbolo = inicializar_especiales(ESPECIALES,CANT_FILAS,CANT_COLUMNAS,posiciones_serpiente,POSICION_OBSTACULOS,posicion_fruta,tablero)
		
		clear_terminal()
		tablero = actualizar_tablero(CANT_FILAS, CANT_COLUMNAS)
		actualizar_obstaculos(tablero, POSICION_OBSTACULOS)
		posicion_especial = (valor_1, valor_2)
		actualizar_fruta(tablero, posicion_fruta)
		actualizar_serpiente(tablero, posiciones_serpiente, CANT_FILAS, CANT_COLUMNAS)
		tablero = actualizar_especial(tablero, posicion_especial,simbolo)
		imprimir_nivel(NIVEL_ACTUAL)
		imprimir_tablero(tablero)
		movimientos_validos()
		imprimir_mochila(MOCHILA)
		
main()

#Esto es para que el usuario decida si quiere volver a jugar.
while True:
	if confirmar_reiniciar_juego():

		main()
	else:
		gracias()
		break





