def dibuja_primer_tablero():
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

def dibuja_tablero():

    print("---------")
    print("|" , matriz[0][0] , matriz[0][1] , matriz[0][2], "|")
    print("|" , matriz[1][0] , matriz[1][1] , matriz[1][2], "|")
    print("|" , matriz[2][0] , matriz[2][1] , matriz[2][2], "|")
    print("---------")


#analizamos el juego

def check_game():
    ended = False
    x_wins = False
    o_wins = False
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
        ended = True
    else:
        if x_wins == True:
            print("X wins")
            ended = True
        if o_wins == True:
            print("O wins")
            ended = True
        if x_wins == False and o_wins == False:
            if vacias == False:
                print("Draw")
                ended = True
    return ended

def ask_coordinates():
    global movement_x
    global movement_y
    global correct_movement
    movements = input("Enter the coordinates:")
    movements = movements.split()
    movement_x_string = movements[0]
    movement_y_string = movements[1]

    if movement_x_string.isnumeric() == False or movement_y_string.isnumeric() == False:
        print("You should enter numbers!")
    else:
        movement_x = int(movement_x_string)
        movement_y = int(movement_y_string)
        if movement_x > 3 or movement_x <1 or movement_y > 3 or movement_y < 1:
            print("Coordinates should be from 1 to 3!")
        else:
            # debo chequear si sigue libre
            libre = False
            if matriz[movement_x - 1][movement_y - 1] == "_" or matriz[movement_x - 1][movement_y - 1] == " ":
                libre = True
            if libre == True:
                correct_movement = True
            else:
                print("This cell is occupied! Choose another one!")


# write your code here
# game = input("Enter cells:")

#initial game
game = "_________"
game_list = list(game)
matriz = []
movement_x = 0
movement_y = 0
player = "X"
correct_movement = False
finalizado = False

dibuja_primer_tablero()

while finalizado == False:
    while correct_movement == False:
        ask_coordinates()

    # tenemos un movimiento válido
    matriz[movement_x - 1][movement_y - 1] = player
    correct_movement = False

    #cambiamos de jugador
    player = "X" if player == "O" else "O"

    dibuja_tablero()

    finalizado = check_game()

