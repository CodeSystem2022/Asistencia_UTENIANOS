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

######################################################################################
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

######################################################################################
# Walter David Torres
# Ejercicio "Clase Cubo"

class Cubo:
    """
    Crear la clase cubo con los atributos, ancho, alto, profundidad, con
    un método calcular_volumen que tendrá la fórmula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """

    def _init_(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad


ancho = int(input('Digite la medida del ancho del cubo: '))
altura = int(input('Digite la medida de la altura del cubo: '))
profundidad = int(input('Digite la medida de la profundidad del cubo: '))
cubo1 = Cubo(ancho, altura, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')

##################################################################################
# Giangrave Facundo
#Ejercicio 4: Calculadora de Impuestos

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a plicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print('El pago con impuesto es: ', pago_con_impuesto)
