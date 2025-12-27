# Variables para llevar el control de las tareas y sus categorías

contadorId = 0       # Contador para asignar un ID único a cada tarea creada
totalTareas = 0      # Contador total de tareas registradas en el sistema

# Contadores individuales para cada categoría de tarea
categoria1 = 0       
categoria2 = 0       
categoria3 = 0       

# Lista con los estados posibles de las tareas y un contador para cuántas hay de cada estado
estadosContador = [
    ["Pendiente", 0],    # Tareas que aún no se han empezado
    ["Activa", 0],      # Tareas que están en proceso
    ["Completada", 0]   # Tareas que ya fueron finalizadas
]

# Lista que almacenará todas las tareas como elementos, cada tarea es una lista con sus datos
tareas = []  
