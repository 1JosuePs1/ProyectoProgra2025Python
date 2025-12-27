import os
os.system('cls')  # limpia la consola al iniciar el programa
from menuPrincipal import menu  # importa la funcion menu desde el archivo menuPrincipal

#usuarios que se pueden probar 
# admin 123
# carlos amador"
# issac rodrigez
# oscar saborio



# lista con usuarios en arreglos 
usuarios = [
    ["admin", "123"],
    ["josue", "rivera"],
    ["carlos", "amador"],
    ["issac", "rodrigez"],
    ["oscar", "saborio"]
]

# ciclo principal del programa
while True:
    print("Bienvenidos al sistema de tareas de Ufidelitas")
    seleccionMenu = input("\n1. Registrar Usuario\n2. Inicio de sesión\nOpción: ")

    # validacion para asegurarse que el input es un numero
    if seleccionMenu == "" or (seleccionMenu < "0" or seleccionMenu > "9"):
        print("Por favor, ingrese solo números.")
        continue

    # convertir la opcion a entero
    seleccionMenu = int(seleccionMenu)

    # opcion para registrar un nuevo usuario
    if seleccionMenu == 1:
        print("")
        usuarioNuevo = input("Ingrese su usuario: ")
        claveNueva = input("Ingrese su clave: ")

        # verificar si el usuario ya existe
        usuarioExistente = False
        for usuarioRegistrado in usuarios:
            if usuarioRegistrado[0] == usuarioNuevo:
                usuarioExistente = True
                break
        
        # si el usuario existe muestra mensaje, si no lo agrega a la lista
        if usuarioExistente:
            print("\nEse nombre de usuario ya está en uso. Intente con otro.")
        else:
            usuarios.append([usuarioNuevo, claveNueva])
            print("\n¡Usuario registrado con éxito!")

    # opcion para inicio de sesion
    elif seleccionMenu == 2:    
        intentosLogin = 0  # contador de intentos fallidos
        while intentosLogin < 3:
            print("")
            usuarioInput = input("Ingrese su usuario: ")
            claveInput = input("Ingrese su clave: ")
            
            # verificar si las credenciales coinciden con algun usuario
            credencialesCorrectas = False
            for usuario in usuarios:
                if usuario[0] == usuarioInput and usuario[1] == claveInput:
                    credencialesCorrectas = True
                    break 
            
            # si las credenciales son correctas accede al menu principal
            if credencialesCorrectas:
                print("\n¡Clave correcta, bienvenido!") 
                menu()
                break  
            else:
                intentosLogin += 1
                print(f"\nUsuario o clave incorrecta. Le quedan {3 - intentosLogin} intentos.")

        # si supera el limite de intentos se cierra el programa
        if intentosLogin == 3:
            print("\nHa superado el límite de intentos. El programa se cerrará.")
            break 

    # si la opcion no es valida muestra mensaje
    else:
        print("Opción no válida. Intente de nuevo.")
