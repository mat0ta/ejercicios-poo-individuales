import random
import string

empresa = {}
edificios = ['A', 'B', 'C']
ciudades = ['New York', 'New york', 'Los Angeles']
empleados = ['Martin', 'Salim', 'Xing']

def crearPropiedades():
    for i in range(3):
        nombre = edificios[i]
        empresa[nombre] = {
            'localicacion': ciudades[i],
            'empleados': empleados
        }
    print(empresa)



crearPropiedades()