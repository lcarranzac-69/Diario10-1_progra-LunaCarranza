#Sistema de control de aforo del cenac
#Autor: Luna Carranza
#Fecha:2026/07/21
CAPACIDAD_MAXIMA = 700
UMBRAL_PREVENTIVO = 560

gupos_aceptados = []
grupos_rechazados = []
ocupacion_actual = 0

print("CONTROL DE INGRESO -ANFITEATRO DEL CENAC")
print("Capacidad máxima: 700 personas")
print("Escriba 'fin' para cerrar el programa")

entrada = input("Cantidad de personas del grupo: ").lower().strip()

while entrada != 'fin':
    try:
        cantidad_grupo = int(entrada)
    except ValueError:
        print("Entrada inválida. escriba un número o 'fin' ")
        
    else:
        if cantidad_grupo < 0 :
            print("ERROR: Cantidad  de personas no válida")
        elif cantidad_grupo +ocupacion_actual <= CAPACIDAD_MAXIMA:
            grupos-aceptados.append(cantidad_grupo)
            ocupacion_actual += cantidad_grupo
            espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
            print(f"Grupo aceptado: ingresan {cantidad_grupo} personas. ")
            print(f"Ocupacion actual: {ocupacion_actual}")
            print(f"Espacios disponibles {espacios_disponibles}")
        else: 
            grupos_rechazados.append(cantidad_grupo)
            espacios_disponibles = CAPACIDAD_MAXIMA -ocupacion_actual
            print(f"Grupo rechazado: no hay espacio para {cantidad_prupo}personas")
            print(f"Ocupacion actual: {ocupacion_actual}")
            print(f"espasios dísponibles {espacios_disponibles}")
    entrada = input("Cantidad de personas del grupo: ").lower().strip()
    
    