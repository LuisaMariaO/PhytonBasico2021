#Comparacion de contraseñas
print("___________________EJERCICIO 1__________________")
password=input("Ingrese una contraseña: ")
confirmacion=input("Confirme la contraseña: ")
if password.lower()==confirmacion.lower():
    print("Confirmacion exitosa")
else:
    print("Las contraseñas no coinciden")

#Grupos de personas
print("___________________EJERCICIO 2__________________")

nombre=input("Ingrese su nombre: ")
sexo=input("Ingrese su sexo: (F si es femenino, M si es masculino ): ")

if nombre[0].lower()<"m" and sexo.upper() =="F":
    print("Perteces al grupo A")
elif nombre[0].lower()>"n" and sexo.upper()=="M":
    print("Perteces al grupo A")
else:
    print("Perteneces al grupo B")




