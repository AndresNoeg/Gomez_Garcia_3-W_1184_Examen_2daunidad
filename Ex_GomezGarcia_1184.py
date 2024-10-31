print(" ")
print("Gomez Garcia Andres Noe 1184: Examen")
print(" ")

#Pide al usuario las materias y las registra en una variable
materia1=input(str("Ingrese la primera materia: "))
materia2 = input(str("Ingrese la segunda materia: "))
materia3 = input(str("Ingrese la tercera materia: "))
materia4 = input(str("Ingrese la cuarta materia: "))
print(" ")

#Junta las 4 variables en una lista
Materias=[materia1,materia2,materia3,materia4]
#imprime la lista
print(Materias)
print(" ")

#Pide al usuario las calificaciones y las registra en una variable
califa1=float(input("Ingrese la calificacion que saco en la primera materia de la lista "))
califa2=float(input("Ingrese la calificacion que saco en la segunda materia de la lista "))
califa3=float(input("Ingrese la calificacion que saco en la tercera materia de la lista "))
califa4=float(input("Ingrese la calificacion que saco en la cuarta materia de la lista "))
print(" ")

#Imprime las materias y la calificacion
print("En ",Materias[0], " saco  ", califa1)
print("En ",Materias[1], " saco  ", califa2)
print("En ",Materias[2], " saco  ", califa3)
print("En ",Materias[3], " saco  ", califa4)
print(" ")

'''
Si una de las calificaciones es igual 
o menor a 5 el mensaje "El alumno repro x materia" 
y "El alumno debera repetirla"  aparecera
'''
if califa1<= 5:
    print("El alumno reprobo", Materias[0])
    print("El alumno debera repetirla ")
    print(" ")

if califa2<= 5:
    print("El alumno reprobo", Materias[1])
    print("El alumno debera repetirla ")
    print(" ")

if califa3<= 5:
    print("El alumno reprobo", Materias[2])
    print("El alumno debera repetirla ")
    print(" ")

if califa4<= 5:
    print("El alumno reprobo", Materias[3])
    print("El alumno debera repetirla ")
    print(" ")

#Imprime que se removera una materia
print(materia3, "Sera removida de la lista")

#Remueve una de las materias de la lista
Materias.remove(materia3)

#Imprime la lista con la materia removida
print(Materias)