print("Ejercicio 1: Triángulo rectángulo")
#Solicito y almaceno la altura del triángulo
h=int(input("Ingresela altrua del triángulo (numero entero positivo): "))
#Impresión del triángulo
for i in range(1,(h+1),1):
     print (i*"*")

print("----------------------------------------")
print("Ejercicio 2: Cuenta regresiva")
#Solicito el número
n=int(input("Ingrese un número: "))

#Imprimo la cuenta regresiva
print(n,end="")
#Imprimo primero n
n=n-1
while n>=0:
    #Imprimo primero la coma, para evitar que quede una coma al final del último número
    print(",",n,end="")
    n=n-1
print("\n")
print("----------------------------------------")
print("Ejercicio 3: Números primos")
#Solicito el número
x=int(input("Ingrese un número: "))
i=2
primo=True
while i<=1000: #Considero los números hasta el 1000
    if x % i == 0 and x!=i:
        primo=False
        break 
    else:
        i=i+1
        continue
#Imprimo el resultado obtenido
if primo==False:
    print(x,"es un número compuesto")
else:
    print(x,"es un numero primo")


