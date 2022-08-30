
n = input("Ingrese numero: ")
n = int(n)

suma = 0

for number in range(0, n+1, 1):
    suma = suma + number
    
print("Valor de la suma: ", suma)