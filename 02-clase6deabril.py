'''
#01-DATOS DE TIPO NUMERICO

edad = 29 #entero

estatura = 1.71 #real

peso = 70.5 #real

complejo = 1 +4j #complejo, se pone j para los complejos

print("Impresion del numero complejo:",complejo,"\n")

print(f"mi estatura es de {estatura}")

# Operacion aritmetica basica para sacr el imc

imc = peso/estatura**2

# Transformando real a entero
print(peso)
print("transformando un valor real a entero",int(peso))

print(edad)
print("transformando entero a real",float(edad))
print("mi IMC es de:",imc)

#el codigo {:.2f} es para aproximar y va entre comillas y .format es para

print("mi IMC es de {:.2f}".format(imc), "\n")

#02-datos de tipos de cadena de caracter
asignatura = "programacion"

carrera = "ingenieria civil en informatica"

print("la asignatura de",asignatura,"corresponde a la carrera de",carrera)

print("la asignatura de",len(asignatura),"corresponde a la carrera de",len(carrera))

#funciones proppias de python
#str() , int() , float() , len() , type()= string es para texto, Int para enteros, float para reales,
#y len cuenta los caracteres, por ej:"hola"=4

#utilizando la funcion len (cuenta la cantidad de caracteres)


#valores booleanos
ampolleta = False
interruptor = True

#con type sabemos el tipo de datos que estamos tratando
print(type(ampolleta))

ampolleta = "soy una ampolleta"
print(type(ampolleta))
# datos de tipos array (objetos de tipo coleccion)

estudiantes = ["matias","marco","cristobal","sebastian"]
num = [1,2,3,4,5,6]
lenguaje = ["python"]
data= ["osorno", {"UV": "nivel bajo", "Temp °c": 15}, (-40.5725, -70.432)]
listamixta = ["felipe", 100, True]

print(data)
print(len(data))
print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:",num)
print("lista de elementos:",lenguaje)

print(estudiantes.count("matias"))


nueva_lista = list()
print("esta es una lista vacia",nueva_lista)



#¿como accedo a un elemento especifico
print(estudiantes[0])
print(estudiantes[1])
#reasignando el valor de la posicion 3 de la lista
estudiantes[0] = "gabriela"
print(estudiantes[0])


data_asig = [10023, "programacion",1,True]


cod,ramo,semestre,estado= data_asig
print(ramo)

#
print(list("python"))
print(list(range(10,21)))
print("\n")
'''

#05 -TUPLAS- (no son mutables)
newtupla = tuple()
grupo1 = ("daniel","cristian","felipe",200,100,"daniel")
print("######## 05-TUPLAS-########")
print(type(grupo1))

#accediendo al primer elemento de la tupla
print(grupo1[0])

print("el elemento se repite:",grupo1.count("daniel"))


print("indice del elemento:",grupo1.index("daniel"))

#reasignando el primer elemento de la tupla 
"""grupo1[0]="constanza"
print(grupo1)"""

#¿se puede sumar las tuplas?


#obteniendo los trozos de la tupla
grupo2 = ("pedro",100,"felipe","diego",2020,"alejandra")
print("trozo de la tupla",grupo1[0:3])

#¿entoces como puedo modificar la tupla , que puedo hacer?



grupo1 = list(grupo1)
print("la tupla ahora es de tipo",type(grupo1),"\n")
print("\n")

'''
#06 - SETS (conjuntos)

conjunto_vacio  = set()
conjunto_vacio1 = {}#¿diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"}) #utilizando funcion set
conjunto_animales = {"Gato","Perro","Loro"}     # utilizando corchetes

print("######## 06-SETS ########")
print(type(conjunto_colores))
print(type(conjunto_animales))
print("el primer set contiene los siguientes colores:",conjunto_colores)

print("El segundo set contiene los siguientes animales:",conjunto_animales)


conjunto_colores.add("celeste")
print("el set de colores se conforman:",conjunto_colores)


print("el set de animales los conforman:",conjunto_animales)



""" -------Diccionarios------ """
diccionari1=dict()
diccionario2={}
datos_personales={
    "Nombre":"Nicolás",
    "Institución":"Ulagos",
    "Edad": 29,
    "Asignaturas": {"Estructura de Datos", "Programación"}
    }
print("Diccionario inicial:",datos_personales)
#Clave es lo mismo que un campo
#Consulta la cantidad de elementos del Diccionario
imprimir(len(datos_personales))
#Como acceder a un elemento especifico de una lista?
print(datos_personales["Institución"])
#Como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["Institución"] = "USS"
#Agregando un nuevo campo al diccionario
datos_personales["Ciudad"] = "Osorno"
imprimir(datos_personales)
#Eliminando un campo del diccionario
del datos_personales["Ciudad"]
print("Diccionario con el campo eliminado:",datos_personales)
'''







