print("Calculadora de Indice de nasa corporal (IMC)")
#Almacenamiento del pesp
peso=input("Ingresa tu peso en kilogramos:")
#Almacenamiento de la estatura
estatura=input("Ingresa tu estatura en metros")
#Calculo del imc
imc=round((float(peso)/float(estatura)**2),2)
#Impresion del resultado
print("Tu indice de masa corporal es: ",imc)

