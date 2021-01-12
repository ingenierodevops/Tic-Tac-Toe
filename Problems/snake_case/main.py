cadena = input()
cadena_snake = ""
indice = 0
for caracter in cadena:
    if caracter.isupper():
        caracter = caracter.lower()
        if indice != 0:
            caracter = "_" + caracter
    cadena_snake += caracter
    indice += 1
print(cadena_snake)
