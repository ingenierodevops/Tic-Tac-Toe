# write your code here
game = input("Enter cells:")
game_list = list(game)
matriz = []
x_wins = False
o_wins = False



for n in range(3):
    indice = 0
    matriz.append([])
    for y in range(3):
        matriz[n].append(game_list[indice + (n * 3)])
        indice += 1

print("---------")
print("|" , matriz[0][0] , matriz[0][1] , matriz[0][2], "|")
print("|" , matriz[1][0] , matriz[1][1] , matriz[1][2], "|")
print("|" , matriz[2][0] , matriz[2][1] , matriz[2][2], "|")
print("---------")

#analizamos el juego

#primero las filas
for fila in matriz:
    if fila[0] == fila[1] == fila[2]:
        if fila[0] == 'X':
            x_wins = True
        else:
            if fila[0] == 'O':
                o_wins = True

#ahora las diagonales
#diagonal 1
indice_filas = 0
diagonal = True
while indice_filas < (len(matriz) - 1):
    if (matriz[indice_filas][indice_filas] != matriz[indice_filas + 1][indice_filas + 1]):
        diagonal = False
    indice_filas += 1
if diagonal == True:
    if matriz[0][0] == 'X':
        x_wins = True
    else:
        if matriz[0][0] == 'O':
            o_wins = True
#diagonal 2
indice_filas = 0
diagonal2 = True
while indice_filas < (len(matriz) - 1):
    if (matriz[indice_filas][(len(matriz) - 1) - indice_filas] != matriz[indice_filas + 1][(len(matriz) - 1) - (indice_filas + 1)]):
        diagonal2 = False
    indice_filas += 1
if diagonal2 == True:
    if matriz[0][len(matriz) - 1] == 'X':
        x_wins = True
    else:
        if matriz[0][len(matriz) - 1] == 'O':
            o_wins = True

# ahora revisamos las columnas
# todo conseguir que sea también independiente de la longitud, está hardcodeado a 3

indice_columnas = 0
while indice_columnas <= (len(matriz) - 1):
    columna = True
    if (matriz[0][indice_columnas] != matriz[1][indice_columnas]):
        columna = False
    else:
        if (matriz[1][indice_columnas] != matriz[2][indice_columnas]):
            columna = False
    if (columna == True):
        if matriz[0][indice_columnas] == 'X':
            x_wins = True
        else:
            if matriz[0][indice_columnas] == 'O':
                o_wins = True
    indice_columnas += 1


# buscamos celdas vacias y contamos oes y xes
vacias = False
oes = 0
xes = 0
for fila in matriz:
    for celda in fila:
        if celda == "O": oes += 1
        if celda == "X": xes += 1
        if celda == "_": vacias = True

if x_wins == True and o_wins == True or (abs(oes - xes) >= 2):
    print("Impossible")
else:
    if x_wins == True:
        print("X wins")
    if o_wins == True:
        print("O wins")
    if x_wins == False and o_wins == False:
        if vacias == True:
            print("Game not finished")
        else:
            print("Draw")