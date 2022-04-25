""""Programa No. 9:
para ingresar un numero y identificar si es par o no"""

print("---------------------------------------------")
print("-----------------Par o Impar-----------------")
print("---------------------------------------------")

#Input
x = int(input("Ingrese el valor de un numero entero: "))

#processing
r=x%2
if r==0:
    msj = "es par"
else:
    msj = "es impar"

#Output
print("El numero " + str(x), msj)
