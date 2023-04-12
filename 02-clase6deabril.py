#01-DATOS DE TIPO NUMERICO
edad = 29 #entero
estatura = 1.71 #real
peso = 70 #real
complejo = 1 +4j #complejo

print("Impresion del numero complejo:",complejo)
#operacion de aritmetica basica
imc = peso/estatura**2
print("mi IMC es de:",imc)

print("mi IMC es de {:.2f}".format(imc))

#02-datos de tipos de cadena de caracter
asignatura = "programacion"
carrera = "ingenieria civil en informatica"
print("la asignatura de",asignatura,"corresponde a la carrera de",carrera)
print("la asignatura de",len(asignatura),"corresponde a la carrera de",len(carrera))

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
print(data)
print(len(data))
print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:",num)
print("lista de elementos:",lenguaje)

print(estudiantes.count("matias"))


nueva_lista = list()
print("esta es una lista vacia",nueva_lista)




print(estudiantes[0])
print(estudiantes[1])

estudiantes[0] = "gabriela"
print(estudiantes[0])


data_asig = [10023, "programacion",1,True]


cod,ramo,semestre,estado= data_asig
print(ramo)


print(list("python"))
print(list(range(10)))
print("\n")







