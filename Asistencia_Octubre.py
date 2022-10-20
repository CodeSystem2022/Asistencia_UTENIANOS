# Miriam Torres
# Creación de la clase Rectángulo

class Rectangulo:
    """
    Crear una clase llamada Rectángulo, debe tener dos atributos: altura y base
    el nombre del método será calcular_area utilizando la fórmula:
    área = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres
    """

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


base = int(input('Digite el número para la base del rectángulo: '))
altura = int(input('Digite el número para la altura del rectángulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El área del rectángulo es: {rectangulo1.calcular_area()}')


# Carolina Belen Delgado
# Ejercicio 05: Crear una funcion para sumar valores recibidos de tipo numericos,
# Utilizando argumentos variabes args como parametro de a
# Funcion y agregar como resultado a suma de todos os valores pasados
# como argumentos.
# Definimos una funcion.
def sumar_valor(args, in_args=):# Recibimos una cantidad de parametros indefinidos
 result=0
 # Iteramos cada elemento
 for valor in_args:
 result
