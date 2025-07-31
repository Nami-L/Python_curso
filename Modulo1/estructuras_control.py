edad = int(input("Cual es tu edad? \n"))

if edad < 18:
    print("Eres menor de edad")
elif edad > 18 and edad < 60:
    print("Eres un adulto")
elif edad > 15:
    print("Eres mayor de 15 años")
elif edad == 60:
    print("Feliz cumpleaños, tienes 60 años")
else:
    print("Eres un adulto mayor")
print("Fin del programa")
