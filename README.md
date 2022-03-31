<h1 align="center">EJERCICIOS-POO-INDIVIDUALES</h1>

En este [repositorio](https://github.com/mat0ta/ejercicios-poo-individuales) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: [mat0ta](https://github.com/mat0ta).

<h2>Inmortal</h2>

Hacer que la interrogaci�n printee lo ultimo.

La funci�n empleada para crear dicho algoritmo es la siguiente:

```py

class Yin: pass
class Yang:
    def _del_(self):
        print("Yang destruido")

yin = Yin()
yang = Yang()
yin.yang = yang

print(yang)
print(yang is yin.yang)
del(yang)
print("?")


# __del__ no era accesible devido a que era privado por lo que se printeaba después. Al ya no ser privado, se ejecuta en orden.

```

<h2>Dia Siguiente</h2>

Hacer una simulacion en la que unos edificios de una determinada empresa sufren una destruccion al ser destruida la ciudad en la que se encuentran

La funci�n empleada para crear dicho algoritmo es la siguiente:

```py

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

```

<h2>Alternativa</h2>

Realizar una agrupacion en una sola clase del algoritmo de ventanas y paredes de la anterior tarea grupal

La funci�n empleada para crear dicho algoritmo es la siguiente:

```py

casa = {}
orientaciones = ['NORTE', 'SUR', 'ESTE', 'OESTE']
class Casa():
  global casa
  def Paredes(self, orientacion):
    for i in range(len(orientacion)):
      nombre = orientacion[i]
      casa[nombre] = {
          'ventanas': {},
      }
    print(casa)
    Casa().Cristal([['NORTE', 0.5, ''], ['SUR', 1, ''], ['ESTE', 2, ''], ['OESTE', 1, '']])
  def Cristal(self, ventanas):
    dimensiones = []
    for i in range(len(ventanas)):
      nombre = ventanas[i][0]
      casa[nombre]['ventanas'] = {
        'superficie': ventanas[i][1],
        'proteccion': ventanas[i][2]
      }
      dimensiones.append(ventanas[i][1])  
    print(casa)
    Casa().Superficie()
  def Superficie(self):
    total = 0
    for i in range(len(orientaciones)):
      total += casa[orientaciones[i]]['ventanas']['superficie']
    print('Superficie acristalada: ' + str(total))
  def ParedCortina(self, orientacion, tamaño):
    casa[orientacion]['ventanas']['superficie'] += tamaño
    print(casa)
  def ComprobarProteccion(self, orientacion):
    if casa[orientacion]['ventanas']['proteccion'] != '':
      print('Protección en regla.')
    else:
      print('Protección obligatoria no presente.')

```

