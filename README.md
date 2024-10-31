# Gomez_Garcia_3-W_1184_Examen_2daunidad

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
califa3=float(input("Ingrese la calificacion que saco en la tercera materia de la lista"))
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

![image](https://github.com/user-attachments/assets/6f1f583e-ce1c-459e-b816-23bd7a4e4abe)

![image](https://github.com/user-attachments/assets/8b9a4453-ff38-44db-a0bf-b908f88f247e)

![image](https://github.com/user-attachments/assets/2b2636ae-64a0-4d02-bc7a-a89b4229071c)

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

![image](https://github.com/user-attachments/assets/6d25256c-4bc6-4d8a-accb-98032c1a1ec8)

![image](https://github.com/user-attachments/assets/27b54548-345a-4740-88a1-60a29ef08bc7)


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

![image](https://github.com/user-attachments/assets/424d1a95-b0bf-4191-bd18-3936a2341083)

![image](https://github.com/user-attachments/assets/d57a67ae-6d50-4cbe-8620-6bfd9b4df0b1)


print(" ")
print("Gomez Garcia Andres Noe 1184: Examen")
print(" ")

#Abre diccionario vacio
datos_personales={}

#Le pide al usuario sus datos
nombre=str(input("Ingrese su nombre: "))
años=int(input("Ingrese su edad: "))
numero_telefono=int(input("Ingrese su numero de telefono: "))
direccion=str(input("ingrese su direccion: "))

#Actualiza el diccionario vacio con los datos nuevos
datos_personales.update({"Nombre:": nombre})
datos_personales.update({"Edad:": años})
datos_personales.update({"Telefono:": numero_telefono})
datos_personales.update({"Direccion:": direccion})

#bucle for para imprimir los 2 datos del diccionario
for x,y in datos_personales.items():
    print(x,y)

![image](https://github.com/user-attachments/assets/6a6dd93e-8bb8-417f-aabd-f419be9b6469)

![image](https://github.com/user-attachments/assets/dc3082c0-1a17-4bfe-8db3-36c3c87a26b4)








