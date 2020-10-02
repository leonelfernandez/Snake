from terminal import timed_input
from terminal import clear_terminal
from capa_visual import *
from capa_logica import *
from capa_interaccion_usuario import *
def main():
	"""Llama a todas las funciones, para asi correr el juego"""
	posiciones_serpiente = [(0, 0, "abajo")]
	tablero = actualizar_tablero()
	posicion_fruta = inicializar_fruta(posiciones_serpiente)
	actualizar_serpiente(tablero, posiciones_serpiente)
	imprimir_tablero(tablero)

	while True:
		direccion = obtener_direccion()
		hay_fruta = mover_serpiente(posicion_fruta, direccion, posiciones_serpiente)
		if hay_fruta:
			posicion_fruta = inicializar_fruta(posiciones_serpiente)
		clear_terminal()
		tablero = actualizar_tablero()
		actualizar_serpiente(tablero, posiciones_serpiente)
		actualizar_fruta(tablero, posicion_fruta)
		imprimir_tablero(tablero)
		if me_comi_el_cuerpo(posiciones_serpiente) or me_comi_la_pared(posiciones_serpiente):
			perdiste()
			break
		if len(posiciones_serpiente) == TAMAÑO_FINAL_SERPIENTE:
			ganaste()
			break
		movimientos_validos()
main()
#Esto es para que el usuario decida si quiere volver a jugar.
while True:
	if reiniciar_juego():
		main()
	else:
		gracias()
		break





