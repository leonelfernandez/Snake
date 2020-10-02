from terminal import timed_input
def obtener_direccion():
    """La funcion recibe la entrada del usuario y determina el movimiento de la serpiente"""
    tecla_actual = ""
    entrada_usuario = timed_input(1)
    direccion = ""
    if not entrada_usuario == "":
        tecla_actual = entrada_usuario[0]
        if not tecla_actual in "awsd":
            tecla_actual = ""
    if tecla_actual == "w":
        direccion = "arriba"
    if tecla_actual == "s":
        direccion = "abajo"
    if tecla_actual == "a":
        direccion = "izquierda"
    if tecla_actual == "d":
        direccion = "derecha"
    return direccion

def reiniciar_juego():
    """Pregunta al usuario si desea volver a jugar, en caso de que diga que si devuelve True,
    y en caso contrario False"""
    usuario = str(input("Desea volver a jugar?[SI/NO]: "))
    if usuario == "si".lower() or usuario == "si".upper():
        return True
    elif usuario == "no".lower() or usuario == "no".upper():
        return False



