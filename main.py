from util import *
from personaje import Personaje
from escenario import Habitacion

log = []


def mainloop(char):
    run = 1
    global habitacion

    comando = input('> ')
    log.append(comando.upper())

    split = comando.split()
    cmd, o = split[0], split[1] if len(split) > 1 else None
    if cmd.lower() == "agarrar":
        agarrable = habitacion[o.upper()]
        if agarrable:
            char.agarrar(habitacion.objetos[o.upper()])
        else:
            print('No puedo agarrar eso')

    elif cmd.lower() == "este":
        char.este()

    elif cmd.lower() == "oeste":
        char.oeste(habitacion)

    elif cmd.lower() == "usar":
        char.usar(o.upper(), habitacion)

    elif cmd.lower() == "examinar":
        char.examinar(habitacion.objetos[o.upper()])

    elif cmd.lower() == "mirar":
        char.mirar(habitacion)

    elif cmd.lower() == "inventario":
        char.inventario()

    elif cmd.lower() == "info":
        info()

    elif cmd.lower() == "salir":
        run = salir()

    posicion = char.posicion
    if posicion not in habitaciones:
        habitacion = Habitacion(posicion)
        habitaciones[posicion] = habitacion
    else:
        habitacion = habitaciones[posicion]

    return run


running = 1
habitaciones = {}
if __name__ == "__main__":
    character = Personaje()
    habitaciones[character.posicion] = Habitacion(character.posicion)
    habitacion = habitaciones[character.posicion]
    while running:
        running = mainloop(character)
    print(log)
