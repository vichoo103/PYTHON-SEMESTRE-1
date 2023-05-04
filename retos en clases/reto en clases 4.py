
persona=input("ingrese el nombre del primer paciente: ")
edad=int(input("ingrese la edad del paciente: "))
if edad<=0 or edad>=150:
  print("ingrese la edad validad del paciente: ")
  edad=(input("ingrese la edad del paciente: "))
peso=float(input("ingrese el peso del primer paciente: "))
estatura=float(input("ingrese la estatura del primer paciente. "))
if estatura <= 0:
  print("ingrese una estatura valida del paciente")
  estatura=(input("ingrese la estatura del primer paciente. "))
 
tuple_1=(persona, edad, peso, estatura) 
print(tuple_1)


persona2=input("ingrese el nombre del segundo paciente: ")
edad2=int(input("ingrese la edad del paciente: "))
if edad2<=0 or edad2>=150:
  print("ingrese la edad validad del paciente: ")
  edad2=int(input("ingrese la edad del paciente: "))
peso2=float(input("ingrese el peso del segundo paciente: "))
estatura2=float(input("ingrese la estatura del segundo paciente. "))
if estatura2 <= 0:
  print("ingrese una estatura valida del paciente")
  estatura2=(input("ingrese la estatura del segundo paciente. "))

tuple_2=(persona2, edad2, peso2, estatura2) 
print(tuple_2)


persona3=input("ingrese el nombre del primer paciente: ")
edad3=int(input("ingrese la edad del paciente: "))
if edad3<=0 or edad3>=150 :
  print("ingrese la edad validad del paciente: ")
  edad3=int(input("ingrese la edad del paciente: "))
peso3=float(input("ingrese el peso del primer paciente: "))
estatura3=float(input("ingrese la estatura del primer paciente. "))
if estatura3 <= 0:
  print("ingrese una estatura valida del paciente")
  estatura3=(input("ingrese la estatura del primer paciente. "))

tuple_3=(persona3, edad3, peso3, estatura3) 
print(tuple_3)


print(tuple_1, tuple_2, tuple_3)