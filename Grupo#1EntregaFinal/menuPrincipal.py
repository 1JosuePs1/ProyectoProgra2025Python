from registroTareas import registroTareasDef  # importa la funcion para registrar tareas
from asignarEstado import seleccionAsignarEstado  # importa la funcion para asignar prioridad y estado
from verTareas import verTareas  # importa la funcion para ver tareas
from informes import seleccionInformes  # importa la funcion para ver informes

# funcion que muestra el menu principal del sistema
def menu():
    global tareas, estadosContador, totalTareas, categoria1, categoria2, categoria3  # variables globales que se usan en varios modulos

    # ciclo para mostrar el menu hasta que el usuario decida salir
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar tarea")
        print("2. Asignar prioridad y estado")
        print("3. Ver tareas activas o pendientes")
        print("4. Ver informes")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción: ")

        # si selecciona registrar tarea
        if opcion == "1":
            print("Registrar tarea")
            registroTareasDef()
        # si selecciona asignar prioridad y estado
        elif opcion == "2":
            print("Asignar prioridad y estado ")
            seleccionAsignarEstado()
        # si selecciona ver tareas
        elif opcion == "3":
            print("Ver tareas activas o pendientes ")
            verTareas()
        # si selecciona ver informes
        elif opcion == "4":
            print("Ver informes ")
            seleccionInformes()
        # si selecciona salir del programa
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        # si ingresa una opcion invalida
        else:
            print("Opción no válida. Intente de nuevo.")
