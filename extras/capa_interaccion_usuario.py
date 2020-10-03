from terminal import timed_input
from capa_logica import asignacion_niveles
def obtener_direccion(velocidad, dif_velocidad):
    """La funcion recibe la entrada del usuario y determina el movimiento de la serpiente"""
    tecla_actual = ""
    entrada_usuario = timed_input(velocidad + dif_velocidad)
    direccion = ""
    poder_especial = ""
    if not entrada_usuario == "":
        tecla_actual = entrada_usuario[0]
        if not tecla_actual in "awsdzxc":
            tecla_actual = ""
    if tecla_actual == "w":
        direccion = "arriba"
    if tecla_actual == "s":
        direccion = "abajo"
    if tecla_actual == "a":
        direccion = "izquierda"
    if tecla_actual == "d":
        direccion = "derecha"
    if tecla_actual == "z":
        poder_especial = "$"
    if tecla_actual == "c":
        poder_especial = "%"
    if tecla_actual == "x":
        poder_especial = "&"
    return direccion, poder_especial

def confirmar_reiniciar_juego():
    """Pregunta al usuario si desea volver a jugar, en caso de que diga que si devuelve True,
    y en caso contrario False"""
    usuario = str(input("Desea volver a jugar?[SI/NO]: "))
    if usuario == "si".lower() or usuario == "si".upper():
        return True
    elif usuario == "no".lower() or usuario == "no".upper():
        return False
        