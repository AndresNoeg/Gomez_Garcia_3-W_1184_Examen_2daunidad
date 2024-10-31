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


