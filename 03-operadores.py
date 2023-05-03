'''
""" 01------OPERADORES ARITMETICOS----------"""
#DECLARANDO VARIABLES DE TIPO ENTERO
un = 20
b = 5
c = 4 
re = 20
"""--------OPERACIONES BASICAS--------"""
x = 2 + 3 # suma
imprimir( x ) # salida: 5

y = 7 - 4 # resta 
imprimir( y ) # salida: 3

z = 5 * 6 # multiplicacion
imprimir( z ) # salida: 30

f = 10 / 2 # division
imprimir( f ) # salida: 5.0

g = 10 // 3 # division entera
imprimir( g ) # salida: 3

h = 2 ** 3 # potencia o elevado
imprimir( h ) # salida: 8

o = 7 % 3 # modulo
imprimir( o ) # salida: 1

#declarando variables de tipo flotante
tiempo = 5.39 #tiempo en SEGUNDO
= 9.81 #la aceleracion de "gravedad" (METRO POR SEGUNDO)

#operanciones artimeticas con flotantes
velocidad = "gravedad" * tiempo
print(f"la velocidad del objeto en caida libre es: {velocidad}m/s" )
print("la velocidad de caida libre es de: {:.2f}".format(velocidad), "m/s" )
print(f"la velocidad de el objeto en caida libre es de: {velocidad :.2f} m/s" )
print("la velocidad del objeto en caida libre es de:" , "%.2f" % velocidad , "m/s" )

#declarando variables de tipo complejo
c1 = 4 + 3j
imprimir(escribir( c1 ))

#creando un numero complejo con complejo
c2 = complejo(3, -5)
print("el numero complejo es:",c2)

print(2c.real) #obteniendo la parte real del numero complejo
print(c2.imag) #obteniendo la parte imaginaria del numero complejo

#¿se puede realizar esta operacion? ¿multplicar una cadena por un entero?
print("hola" + 5)
#y la siguiete multiplicacion?
"""print("hola" * 3.5*2)""" #No por que nos pasamos un poco poniendo enteros, flotantes y string.
# y esta?
print("Hola" * (int((10*2)/5))," \n ") #Si, porque da un numero entero y no se dejan flotantes

#y por ultimo esta?
#print("hola" + 20)
print("Hola" + str(20))
"""########### 02-OPERADORES DE COMPARACION ##########"""

#comparando terminos numericos
print("Comparando numeros")
imprimir(a==b) #Igual a
print(a != b) #Desigual a
print(a > b) #Alcalde a
imprimir(a < b) #Menor a
print(c >= d) #Mayor o igual a
print(c <= d) #Menor o igual a
imprimir(" \n ")

#Comparando cadenas de caracteres
animal_domestico="gato"
animal_salvaje="leopardo"
print("Comparando cadenas de caracteres")
print(animal_domestico == animal_salvaje) # Igual a
print(animal_domestico != animal_salvaje) # Desigual a
print(animal_domestico > animal_salvaje) # Mayor a
print(animal_domestico < animal_salvaje) # Menor a
print(animal_salvaje >= animal_domestico) # Mayor o igual a
print(animal_salvaje <= animal_domestico) # Menor o igual a

Bencina = Cierto
encendido = Verdadero
edad= 19
imprimir(bool(bencina))
print(bool(not bencina)) #Se transforma en False, y si fuera False se transformaria en True
#Utilizando el operador AND
si bencina y encendido:
    print("El vehiculo puede avanzar")
demás:
    print("El vehiculo no puede arrancar")
#Utilizando el operador OR
si bencina o (encendido o edad>=18):
    print("El vehiculo puede avanzar")
demás:
    print("El vehiculo no puede arrancar")
#Utilizando el operador NOT junto al AND
si no bencina y encendido:
    print("El vehiculo puede avanzar")
demás:
    print("El vehiculo no puede arrancar")

'''
