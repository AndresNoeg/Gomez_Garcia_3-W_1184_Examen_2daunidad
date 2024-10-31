print(" ")
print("Gomez Garcia Andres Noe 1184: Examen")
print(" ")

#Abre diccionario vacio
Asignaturas={}

#Pide al usuario las materias y las registra en una variable
materia1=input(str("Ingrese la primera materia: "))
materia2 = input(str("Ingrese la segunda materia: "))
materia3 = input(str("Ingrese la tercera materia: "))
materia4 = input(str("Ingrese la cuarta materia: "))
print(" ")

#Pide al usuario las calificaciones y las registra en una variable
califa1=float(input("Ingrese la calificacion que saco en la primera materia de la lista "))
califa2=float(input("Ingrese la calificacion que saco en la segunda materia de la lista "))
califa3=float(input("Ingrese la calificacion que saco en la tercera materia de la lista "))
califa4=float(input("Ingrese la calificacion que saco en la cuarta materia de la lista "))
print(" ")

#Actualiza el diccionario y agrega las variables
Asignaturas.update({materia1:califa1})
Asignaturas.update({materia2:califa2})
Asignaturas.update({materia3:califa3})
Asignaturas.update({materia4:califa4})

#Bucle for para mostrar materia y calificacion
for x,y in Asignaturas.items():
    print(x,y)

#Suma la calificacion de las materias
r=califa1+califa2+califa3+califa4

#Muestra la cantidad total de puntos en todas las materias
print("El total de puntos en todas las materias es de: ", r )
