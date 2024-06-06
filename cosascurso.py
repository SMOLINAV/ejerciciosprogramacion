# Tipos de datos
# Tipo numericos:
int ="enteros"
float = "decimales"
'''
podemos saber el tipo de dato de una variable con:
type(variable)
o puede ser hasta de un numero con type(#)
'''
# Tipo texto
str = "representa secuencias o cadenas de caracteres""Lo que quiera se puede tener en string, hasta los numeros si se ponen entre comillas simples o dobles"
# Tipos booleanos
bool = "True o False""para las preguntas que se pueden responder de forma simple""tiene que escribirse con mayuscula la primera letra"

# Calculando valores. Operadores y expresiones
"""
+ = suma
- = resta
* = multiplicacion
/ = division
** = potencia
// = division entera
% = residuo

"""
'''
Tambien estan los 
< = menor que
> = mayor que
<= = menor o igual que
>= = mayor o igual que
== = igual que
!= = distinto que

Estos siempre entregan un boolean

Tambien estan con la negación
siempre dan un boolean 
not = negacion
esta el y o no
y = and  cuandos los dos son verdaderos
o = or cuando uno de los dos es verdadero
'''
# Hay operadores para str
'''
+ = concatenar
* = repetir
'''

# Manipulando datos: conversion de tipos
'''
ejemplo cuando quiero dar que "son las " + (13 + 2)
eso deberia dar error, porque no se puede poner un str con un int
deberia convertir el int a str
daria que lo debo poner str(13+2)

ejemplo cuando quiero dar que "son las " + str(13+2)
iomprimiria = son las 15
'''
'''
tambien se puede converitir cosas a int, por ejemplo
diciendole que convierta int(3.55546)
daria 3
tambien se puede trar un entero de la parte de un str 
ejemplo
diciendole que convierta int("3") + 12
daria 15
Sacaría error si se tiene str con letras:
int("D3 5")
daria error
'''
'''
conviertiendo de int a float
ejemplo
float(3)
daria 3.0
un str con letras da error
float("D3 5")
daria error
a diferencia de float("3")
daria 3.0
'''
"""
se puede convertir bool
bool(0) = false 
bool("") = false
bool(1.5) = true
bool("hola") = true
se puede convertir los false a true...
bool("False") = True
bool("0") = True
"""

# ALmacenar valores. variables y asignaciones
'''
asignar a las variables
ejemplo 
llegada = 14 
precio = 20
entonces por ejemplo 
(19 - llegada) * precio = 100
'''

# Escribiendo en pantalla print
'''
ejemplos
print("hola")
mensaje = "hola"
print(mensaje)
print((3+5)+2)
calculo = (3+5)+2
print(calculo)
'''
'''
Expresiones más complejas como:
episodio = 1
print("episodio ", episodio, " es la mejor")
'''
"""
ejemplos=
nombre = "santi"
edad = 21
print("soy", nombre, end=" ")
print("y tengo", edad, "años")
print("cumplidos")
"""
'''
para cambiar el separador de un print
ejemplo
print("hola", "mundo")
print("hola", "mundo", sep="...")
daria hola...mundo
'''

# Recibiendo datos del usuario input
'''
ejemplo
nombre = input("cual es tu nombre? ")
print("Hola", nombre)
'''
'''
input siempre entrega un str
pero esto se puede cambiar tranquilamente como 
int(input("cual es tu edad? "))
daria 21
que es tipo int
'''
