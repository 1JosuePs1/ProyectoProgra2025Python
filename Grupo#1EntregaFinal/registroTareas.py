import os
os.system('cls')  # limpia la consola
import variables  # importa el archivo variables.py donde estan las variables globales


# funcion para registrar tareas nuevas
def registroTareasDef():
    # variables globales para poder modificarlas desde esta funcion
    global tareas, totalTareas, estadosContador, categoria1, categoria2, categoria3

    # ciclo para que el usuario pueda registrar tareas hasta que decida salir
    while True:
        seleccionMenu = input("\n 1. Registrar nueva tarea\n 2. Menú \n Opción: ")

        # validacion basica para que solo acepte numeros
        if seleccionMenu == "" or (seleccionMenu < "0" or seleccionMenu > "9"):
            print("Por favor, ingrese solo números.")
            continue

        seleccionMenu = int(seleccionMenu)

        # opcion 1 registrar nueva tarea
        if seleccionMenu == 1:
            tarea = []  # lista vacia para guardar los datos de la tarea, las tareas son una lista dentro de listas

            variables.contadorId += 1  # incrementa el id global de tareas
            tareaId = variables.contadorId  # usa el id actual para la nueva tarea

            # se piden los datos de la tarea
            tareaTitulo = input("Ingrese el título de la tarea: ")
            tareaDescripcion = input("Ingrese la descripción de la tarea: ")
            tareaFechaCreacion = input("Ingrese fecha de creacion DD/MM/AA: ")
            tareaFechaEntrega = input("Ingrese fecha de entrega DD/MM/AA: ")
            tareaEstado = "Activa"  # todas las tareas nuevas inician como activas
            tareaPrioridad = input("Prioridad Baja, Media o Alta: ")
            seleccionCategoria = input("Ingrese la categoría: 1.Trabajo/Escuela, 2.Personal/Hogar, 3.Salud/Bienestar: ")

            # se asigna la categoria segun la seleccion del usuario
            if seleccionCategoria == "1":
                tareaCategoria = "Trabajo/Estudio"
                variables.categoria1 += 1
            elif seleccionCategoria == "2":
                tareaCategoria = "Personal/Hogar"
                variables.categoria2 += 1
            elif seleccionCategoria == "3":
                tareaCategoria = "Salud/Bienestar"
                variables.categoria3 += 1
            else:
                tareaCategoria = "Categoría no válida"

            # se guardan todos los datos de la tarea en la lista
            tarea.append(tareaId)
            tarea.append(tareaTitulo)
            tarea.append(tareaDescripcion)
            tarea.append(tareaFechaCreacion)
            tarea.append(tareaFechaEntrega)
            tarea.append(tareaEstado)
            tarea.append(tareaPrioridad)
            tarea.append(tareaCategoria)

            # se agrega la tarea a la lista global de tareas
            variables.tareas.append(tarea)
            variables.totalTareas += 1
            variables.estadosContador[1][1] += 1  # suma 1 al contador de tareas activas

            # se muestran los datos de la tarea registrada
            print("\n Tarea registrada con éxito:")
            print(f"  Tarea #{tarea[0]}")
            print(f"  Título: {tarea[1]}")
            print(f"  Descripción: {tarea[2]}")
            print(f"  Fecha de creación {tarea[3]} - Se entrega el {tarea[4]}")
            print(f"  Estado: {tarea[5]}")
            print(f"  Prioridad: {tarea[6]}")
            print(f"  Categoría: {tarea[7]}")
            print(" ")

        # opcion 2 salir al menu
        elif seleccionMenu == 2:
            break
