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

#Junta las 4 variables en una lista
califas=[califa1,califa2,califa3,califa4]
#imprime la lista
print(califas)
print(" ")

#Imprime las materias y la calificacion
print("En ",Materias[0], " saco  ", califas[0])
print("En ",Materias[1], " saco  ", califas[1])
print("En ",Materias[2], " saco  ", califas[2])
print("En ",Materias[3], " saco  ", califas[3])
print(" ")

