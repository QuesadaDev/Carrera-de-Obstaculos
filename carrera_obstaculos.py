import random
#Este programa realiza una carrera de obstáculos, en el caso de que la acción sea "run" y la pista "_" o "jump" y la
#pista "|" contará como obstáculo superado, en cualquier otro caso no cuenta como obstáculo superado

def selection_option(longitud):

    action_select = ""
    pist_select = ""

    action = "run,jump"
    pist = "_,|"

    options_action = action.split(",")
    options_pist = pist.split(",")

    for i in range(longitud):
        action_select = [random.choice(options_action) for _ in range(longitud)]
        pist_select = [random.choice(options_pist) for _ in range(longitud)]
    return action_select, pist_select


def carrera(accion, pista):

    resultado_carrera = []

    for action, pist in zip(accion, pista):
        if action == "run" and pist == "_":
            resultado_carrera.append("_")
        elif action == "jump" and pist == "|":
            resultado_carrera.append("|")
        elif action == "jump" and pist == "_":
            resultado_carrera.append("x")
        elif action == "run" and pist == "|":
            resultado_carrera.append("/")
        else:
            return False

    resultado_final = "".join(resultado_carrera)
    print("La pista generado ha sido:", resultado_final)
    return "x" not in resultado_final and "/" not in resultado_final


action_select, pist_select = selection_option(5)
resultado = carrera(action_select, pist_select)
print('Si' if resultado else 'No', "ha superado la carrera")
