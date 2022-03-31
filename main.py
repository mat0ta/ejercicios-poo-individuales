import sys
sys.path.insert(1, './modules')
from modules import Alternativa, Diasiguiente, Inmortal
from src.totareadme import readme

array_ejercicios = {
  1: 'Alternativa.Casa()',
  2: 'Diasiguiente.crearPropiedades()'
}

if __name__ == "__main__":
    readme('C:/Users/marti/Documents/GitHub/ejercicios-poo-individuales')
    start = input('Bienvenido a la plataforma de ejercicios de poo. Por favor, introduzca el número del ejercicio que quiere probar (1 a 2) o introduzca 0 para salir: ')
    while int(start) >= 1 and int(start) <= 2:
        eval(str(array_ejercicios[int(start)]))
        start = input('Por favor, introduzca el número del ejercicio que quiere probar (1 a 2) o introduzca 0 para salir: ')