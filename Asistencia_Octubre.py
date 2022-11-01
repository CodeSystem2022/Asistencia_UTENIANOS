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


#------------------------------------------------------------------ SABA JUAN AGUSTIN ------------------------------------------------------------------
class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Definimos el método init con los parámetros
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni  # Este atributo está encapsulado (de una manera sugerida)
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    # El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
    # El método __init__ se llama automáticamente, es decir es imposible olvidarse de llamarlo ya que se llamará
    # automaticamente.
    # Dentro de la clase Persona definimos un método. <self> es el parámetro por default y es la referencia al objeto
    # que se va a crear.
    # Creamos los atributos del objeto Persona dentro de un método sin embargo no son atributos de una clase.
    # No es común asignar valores por default a los atributos como código duro.
    # CÓMO VA A DIFERENCIAR NUESTRO MÉTODO CUÁL ES ELS Y CUÁL ES EL ATRIBUTO Y CUÁL ES LA VARIABLE?
    # self.nombre va a ser el atributo y nombre va a ser la variable.

    def mostrar_detalle(self):  # self es lo mismo que la palabra 'this' en JAVA
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección '
              f'es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Agustin', 'Saba', 35555555, 31)
# La parte izquierda es nuestra variable denominada persona1 que va a contener el objeto de tipo Persona.
# El lado derecho es un constructor que apunta al método init y tiene argumentos el constructor

print(persona1.nombre, persona1.apellido, persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 36666666, 45)

print(persona2.nombre, persona2.apellido, persona2.edad)

# Modificamos los valores de los atributos de persona1
persona1.nombre = 'Nicolas'
persona1.apellido = 'Tarditti'
persona1.edad = '45'

print(persona1.nombre, persona1.apellido, persona1.edad)

persona1.mostrar_detalle()  # La referencia se pasa de manera automática
persona2.mostrar_detalle()

# Persona.mostrar_detalle() Debemos pasarle una referencia para el self o dará error

# EN PYTHON PODEMOS CREAR ATRIBUTOS QUE NO ESTÁN DEFINIDOS EN EL MÉTODO INIT (SUPERFICIALES)$$$$$$$$$$PRÁCTICAS VIEJAS
persona1.telefono = '2614444444'  # creamos el atributo 'SUPERFICIAL' teléfono, es decir, el objeto persona2 no va a
# tener este atributo

print(persona1.telefono)


persona3 = Persona('Rogelio', 'Romero', 37777777, 22, 'Teléfono', '2614444444', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, Cfavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) No se debe utilizar este atributo o se debe tratar con cuidado (ya que está encapsulado)
# persona.__nombre Este atributo está totalmente encapsulado
#--------------------------------------------------------------------------------------------------------------------------------------------------------



#Putrino Agustin


# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado (iva)
# Formula: pago_total = pago_sin_impuesto+ pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 100
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxx

# Creamos la función que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Digite el pago sin impuesto: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto,impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')

************************************************************COSTILLA CELINA PRIMERA PARTE POO****************************************************************************
class Persona: #Creamos una clase
   def __init__(self,nombre,apellido,edad):
     self.nombre= nombre
     self.apellido=apellido
     self.edad= edad
   def mostrar_detalle(self):
      print(f'Persona: {self.nombre}{self.apellido} {self.edad}')


print(Persona)
persona1=Persona("Celina","Costilla",25)
print(persona1.apellido)
print(persona1.nombre)
print(persona1.edad)
persona2=Persona("Ariel","Betancud",35)
print(f'Objeto dos clase Persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')
 
 #Modificar atributos 

persona1.nombre="Liliana"
persona1.apellido="Garzón"
persona1.edad: 45
print(f'Objeto uno clase Persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

*************************************************SEGUNDA PARTE POO*********************************************************
class Aritmetica:
    """
    El nombre de este tipo de comentario es DocString
    Esto es documentacion de la clase en python
    Haremos en esta clase suma, resta ,multiplicacion y más

    """

    def __init__(self,operandoA,operandoB):
        self.operandoA=operandoA
        self.operandoB=operandoB
     #Metodo para sumar
    def sumar(self):
        return self.operandoA+self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB 
    def dividir(self):
        return self.operandoA / self.operandoB       

aritmetica1=Aritmetica(7,9)   # le pasamos los parametros para los operandos     
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'La resta de los números es: {aritmetica1.restar()}') 
print(f'La multiplicación de los números es: {aritmetica1.multiplicar()}') 
print(f'La división de los números es {aritmetica1.dividir():.2f}') 

#Los atributos son características y los métodos son comportamientos que tendrán los objetos
persona1.mostrar_detalle()

# cargar atributos al objeto persona 1
persona1.telefono='123456' #hemos creado un atributo del objeto persona1
print(persona1.telefono)
