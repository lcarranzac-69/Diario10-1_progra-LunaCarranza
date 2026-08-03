"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_promedio(lista):
    """Recibo una lista, la sumo y retorno el promedio"""
    promedio = sum(lista) / len(lista)
    return promedio

def calcular_logro_meta(lista_ventas, meta):
    """Cálcula el porcentaje de logro de la meta"""
    total_ventas = (sum(lista_ventas))
    return (total_ventas * 100) / meta

def calcular_clasificacion(porcentaje):
    if porcentaje >=100:
        mensaje = "Felicidades meta alcanzada, sigue así!"
    elif porcentaje >= 80:
        mensaje = "Llamada de atención, debe trabajar por la meta..!"
    else:
        mensaje = "URGENTE, crisis de ventas. Atención prioritaria"
    return mensaje
def imprimir_reporte(datos_reporte):
    """Imprime el reporte final de ventas por sede"""
    print("\nREPORTE FINAL")
    print("-" * 60)
# Se recorre cada fila del reporte.
for fila in datos_reporte:
    print(f"Sede: {fila['nombre']}")
    print(f"Povincia:{fila['provincia']}")
    print(f"Tipo: {fila['tipo']}")
    print(f"Total semanal: ₡{fila['total']:,.0f}")
    print(f"Promedio diario: ₡{fila['promedio']:,.0f} ")
    print(f"Cumplimiento: {fila['porcentaje']:.2f}%")
    print("Estado: {fila['estado]}")
    print("-" * 60)
    print("Cantidad de sedes:", len(datos_reporte))
#print("Tipo sedes:",type(sedes).__name__)
#print("Cantidad de emprendimiento:", len(sedes))
#primer_emprendimiento = sedes [0]
#print("tipo indice[0]:", type(primer_emprendimiento).__name__)
#print("Emprendimiento:", primer_emprendimiento["nombre"] )
#print("ventas emprendimiento",sum(primer_emprendimiento['ventas']))

reporte ={}
for emprendimiento in sedes:
    ventas = emprendimiento['ventas']
    meta = emprendimiento['meta']
    nombre = emprendimiento['nombre']
    promedio_diario = calcular_promedio(ventas)
    porcentaje_logro = calcular_logro_meta(ventas, meta)
    clasificacion = calcular_clasificacion(porcentaje_logro) #---clasificacion
    
    reporte.appen(
    
    {
        "nombre": nombre,
        "provincia": emprendimiento["provincia"],
        "tipo": emprendimiento["tipo"],
        "total": sum(emprendimiento['ventas']),
        "promedio": promedio_diario,
        "porcentaje": porcentaje_logro,
        "estado": clasificacion
    }
    )                       
#promedio_diario = calcular_promedio(primer_emprendimiento['ventas'])
#porcentaje_logro = calcular_logro_meta(primer_emprendimiento['ventas'], primer_emprendimiento['meta'])
imprimir_reporte(reporte)
    #print(f'\n---Emprendimiento {nombre}---')
    #print("Promedio diario de ventas:", promedio_diario)
    #print("Porcentaje logro:", porcentaje_logro)
    #print("clasificación:" ,clasificacion) 