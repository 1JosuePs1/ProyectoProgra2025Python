import os
import variables  # importa el archivo variables donde estan las variables globales
os.system("cls")  # limpia la consola


# funcion para mostrar el menu de seleccion de informes
def seleccionInformes():
    # ciclo para que el usuario pueda ver informes hasta que decida salir
    while True:
        seleccionMenu = int(input("\n1. Informe Tareas completadas \n2. Informe Tareas por categoría \n3. Menú \nOpción: "))

        # opcion 1 muestra el informe de tareas completadas
        if seleccionMenu == 1:
            informe1()
        # opcion 2 muestra el informe de tareas por categoria
        elif seleccionMenu == 2:
            informe2()
        # opcion 3 vuelve al menu anterior
        elif seleccionMenu == 3:
            break 
        # si no es ninguna de las opciones anteriores muestra error
        else:
            print("Opción no válida.")


# funcion para mostrar el informe de tareas completadas
def informe1():
    print(" ")
    print("Cantidad de tareas creadas:", variables.totalTareas)  # total de tareas creadas
    print("Cantidad de tareas completadas:", variables.estadosContador[2][1])  # cantidad de tareas con estado completada
    print(" ")

    # si hay tareas calcula el porcentaje de tareas completadas
    if variables.totalTareas > 0:
        porcentaje = (variables.estadosContador[2][1] / variables.totalTareas) * 100
        print("Porcentaje de tareas completadas:", porcentaje, "%")
    # si no hay tareas muestra mensaje
    else:
        print("No hay tareas registradas aún.")


# funcion para mostrar el informe de tareas por categoria
def informe2():
    print(" ")
    print("La cantidad de tareas con categoría Trabajo/Estudio son", variables.categoria1)  # total categoria 1
    print(" ")

    print("La cantidad de tareas con categoría Personal/Hogar son", variables.categoria2)  # total categoria 2
    print(" ")

    print("La cantidad de tareas con categoría Salud/Bienestar son", variables.categoria3)  # total categoria 3
    print(" ")
