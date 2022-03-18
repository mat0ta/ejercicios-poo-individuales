edificios = ['A', 'B', 'C']
ciudades = ['New York', 'New York', 'Los Angeles']
empleados = ['Martin', 'Salim', 'Xing']
empresa = {}

def crearPropiedades(propiedades = 3):
    global empresa
    for i in range(propiedades):
        nombre = edificios[i]
        empresa[nombre] = {
            'localizacion': ciudades[i],
            'empleados': empleados,
            'estado': 'En orden'
        }
    print(empresa)
    ciudad = str(input('¿En qué ciudad quieres que ocurra la catástrofe?: '))
    catastrofe(ciudad)

def catastrofe(ciudad):
    global empresa
    for i in range(len(empresa)):
        if empresa[edificios[i]]['localizacion'] == ciudad:
            empresa[edificios[i]]['estado'] = 'Derruido'
            empresa[edificios[i]]['empleados'] = []
    print(empresa)