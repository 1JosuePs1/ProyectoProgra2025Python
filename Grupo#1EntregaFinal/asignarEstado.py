import os
from variables import tareas, estadosContador  # importa lista de tareas y el contador de estados
os.system("cls")  # limpia la consola


# funcion para mostrar el menu de asignar estado o prioridad
def seleccionAsignarEstado():
    # ciclo que repite el menu hasta que el usuario elija salir
    while True:
        seleccionMenu = input("\n1. Cambiar estado de la tarea \n2. Cambiar Prioridad de la tarea \n3. Menu \nOpción: ")
        # validacion para que solo acepte numeros
        if seleccionMenu == "" or (seleccionMenu < "0" or seleccionMenu > "9"):
            print("Por favor, ingrese solo números.")
            continue
        seleccionMenu = int(seleccionMenu)

        # segun la opcion se llama a la funcion correspondiente
        if seleccionMenu == 1:
            cambiarEstado()
        elif seleccionMenu == 2:
            cambiarPrioridad()
        elif seleccionMenu == 3:
            break
        else:
            print("Opción no válida.")


# funcion para cambiar el estado de una tarea
def cambiarEstado():
    # si no hay tareas muestra mensaje y termina
    if not tareas:
        print("No hay tareas registradas.")
        return

    # muestra todas las tareas con su id, titulo y estado
    for tarea in tareas:
        print(" ")
        print(f"  Tarea #{tarea[0]}")
        print(f"  Título: {tarea[1]}")
        print(f"  Estado actual: {tarea[5]}")
        print(" ")

    # pide el id de la tarea a modificar
    seleccionTareas = int(input("\nSeleccione la tarea que quieres cambiarle el estado por su número: "))

    # busca la tarea con el id indicado
    for tarea in tareas:
        if tarea[0] == seleccionTareas:
            print("\nSeleccione el nuevo estado de la tarea:")
            print("1. Pendiente\n2. Activa\n3. Completada")
            print(" ")

            seleccionEstado = int(input("Opción: "))
            estadoActual = tarea[5]

            # asigna el indice del estado actual
            if estadoActual == "Pendiente":
                idActual = 0
            elif estadoActual == "Activa":
                idActual = 1
            elif estadoActual == "Completada":
                idActual = 2
            else:
                idActual = -1

            # indice del estado nuevo
            idNuevo = seleccionEstado - 1

            # si el nuevo estado es diferente y valido actualiza los contadores y el 
            # estado revisa que el numero que representa el estado nuevo sea válido (0 = Pendiente, 1 = Activa, 2 = Completada).
            if idActual != idNuevo and idNuevo in [0, 1, 2]:
                estadosContador[idActual][1] -= 1
                estadosContador[idNuevo][1] += 1
                if idNuevo == 0:
                    tarea[5] = "Pendiente"
                elif idNuevo == 1:
                    tarea[5] = "Activa"
                elif idNuevo == 2:
                    tarea[5] = "Completada"
                print(f"Estado de la tarea #{tarea[0]} {tarea[1]} ha cambiado a {tarea[5]}")
            else:
                print("La tarea ya tiene ese estado o la opción es inválida.")
            return

    # si no encontro la tarea
    print("No se encontró una tarea con ese número")


# funcion para cambiar la prioridad de una tarea
def cambiarPrioridad():
    # si no hay tareas muestra mensaje
    if not tareas:
        print("No hay tareas registradas.")
        return

    # muestra todas las tareas con su id, titulo y prioridad
    for tarea in tareas:
        print(" ")
        print(f"  Tarea #{tarea[0]}")
        print(f"  Título: {tarea[1]}")
        print(f"  Prioridad de la tarea: {tarea[6]}")
        print(" ")

    # pide el id de la tarea a modificar
    seleccionTareas = int(input("\nSeleccione la tarea que quieres cambiarle la prioridad por su número: "))
    print(" ")

    # busca la tarea
    for tarea in tareas:
        if tarea[0] == seleccionTareas:
            print("\nSeleccione la nueva prioridad:")
            print("1. Baja\n2. Media\n3. Alta")
            print(" ")

            seleccionPrioridad = int(input("Opción: "))
            prioridadActual = tarea[6]

            # asigna la nueva prioridad segun la opcion
            if seleccionPrioridad == 1:
                nuevaPrioridad = "Baja"
            elif seleccionPrioridad == 2:
                nuevaPrioridad = "Media"
            elif seleccionPrioridad == 3:
                nuevaPrioridad = "Alta"
            else:
                nuevaPrioridad = ""

            # si es valida y distinta la cambia
            if nuevaPrioridad and prioridadActual != nuevaPrioridad:
                tarea[6] = nuevaPrioridad
                print(f"Prioridad de la tarea #{tarea[0]} {tarea[1]} ha cambiado a {tarea[6]}.")
            elif nuevaPrioridad == "":
                print("Opción inválida.")
            else:
                print("La tarea ya tiene esa prioridad.")
            return

    # si no encuentra la tarea
    print("No se encontró una tarea con ese número")
