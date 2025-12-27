import os 
os.system('cls')

from variables import tareas

# funcion principal para elegir si ver tareas o volver al menu
def seleccionVerTareas():
    while True:
        # menu para ver tareas
        seleccionMenu = int(input("\n1. Ver tareas Pendientes o Activas \n2. Menú \nOpción: "))

        # si selecciona 1 llama a la funcion verTareas
        if seleccionMenu == 1:
            verTareas()
        # si selecciona 2 vuelve al menu anterior
        elif seleccionMenu == 2:
            break 
        # si no es ninguna opcion valida
        else:
            print("Opción no válida.")

# funcion para mostrar las tareas que no estan completadas
def verTareas():
    tareasMostradas = 0  # contador de tareas que se muestran
    
    # recorre todas las tareas guardadas
    for tarea in tareas:
        # si el estado no es completada se muestra la tarea
        if tarea[5] != "Completada":
            print("\n")
            print(f"  Tarea #{tarea[0]}")
            print(f"  Título: {tarea[1]}")
            print(f"  Descripción: {tarea[2]}")
            print(f"  Estado: {tarea[5]}")
            print(f"  Prioridad: {tarea[6]}")
            print(f"  Categoría: {tarea[7]}")
            print(f"  Fecha de creación {tarea[3]} - Se entrega el {tarea[4]}")
            print("\n ")
            tareasMostradas += 1  # aumenta el contador
    
    # si no se mostro ninguna tarea significa que no hay pendientes ni activas
    if tareasMostradas == 0:
        print("No hay tareas pendientes o activas. ")
