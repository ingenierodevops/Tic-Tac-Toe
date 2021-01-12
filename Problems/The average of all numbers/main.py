# put your python code here
a = int(input())
b = int(input())
media = 0
suma = 0
contador = 0
for number in range(a, b):
    if number % 3 == 0:
        suma = suma + number
        contador += 1
if b % 3 == 0:
    suma = suma + b
    contador = contador + 1
media = suma / contador
print(media)