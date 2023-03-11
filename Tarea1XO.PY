print("\n")
print ("\t -------> Bienvenidos al juego tic tac toe <---------     ")
print ("\t             -------> A jugar <---------     ")
###DISE;ANDO TABLERO Python 3X3  tic tac toe Python

 
def tictactoe_grid(value):  
    print("\n")  
    print("\t      |      |")  
    print("\t    {} |  {}   |  {}".format(value[0], value[1], value[2]))  
    print('\t______|______|______')  
# imprimiendo las tres primeras casillas del tablero de juego 3X3
    print("\t      |      |") 
    print("\t   {}  |  {}   |  {}".format(value[3], value[4], value[5]))  
    print('\t______|______|______')  
    print("\t      |      |")  
#  imprimiendo las tres segundas casillas del tablero de juego 3X3 
    print("\t  {}   |  {}   |  {}".format(value[6], value[7], value[8]))  
    print("\t      |      |")  
    print("\n") 
#  imprimiendo las tres ultimas casillas del tablero de juego 3X3 
 
###Para validar la situación ganadora de tic tac toe Python
# Función Python definida por el usuario para validar las combinaciones ganadoras en todo el juego Python de tres en raya

def my_scoreboard(score_board):  
    print("\t------------------------------------------------------------------")  
    print("\t         MARCADOR PARA EL JUEGO TIC TAC TOE PYTHON        ")  
    print("\t------------------------------------------------------------------")  
   
    list_of_the_two_players = list(score_board.keys())  
    print("\t   ", list_of_the_two_players[0], "\t    ", score_board[list_of_the_two_players[0]])  
    print("\t   ", list_of_the_two_players[1], "\t    ", score_board[list_of_the_two_players[1]])  
   
    print("\t-----------------------------------------------------------------\n")
 
###Para validar la situación ganadora de tic tac toe Python
# Función Python definida por el usuario para validar las combinaciones ganadoras en todo el juego Python de tres en raya
def win_validate(position_player, player_current):  
   
 #  A continuación se muestran todas las posibles combinaciones ganadoras que se analizaron para ganar el juego Python de tres en raya 
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  
   
#   usando el bucle for en Python para validar si alguna combinación ganadora se valida como VERDADERA o no
    for i in win_combinations:  
        if all(j in position_player[player_current] for j in i):  
   
#Si cualquier combinación ganadora se valida como VERDADERA, la función devolverá VERDADERA 
            return True  
#  Si alguna combinación ganadora no se valida como VERDADERA, la función devolverá FALSO 
    return False         
   
#   La función definida por el usuario de Python para validar es el tres en raya El juego de Python es un empate
def tie_validate(position_player):  
    if len(position_player['X']) + len(position_player['O']) == 9:  
        return True  
    return False     
        

###Uso de la estructura de datos para almacenar datos para un solo juego de tres en raya Python

def game_single(player_current):  
# función para resaltar el juego de Python tic tac toe
    value = [' ' for i in range(9)]  
       
    print("usando la estructura de datos para almacenar las posiciones ocupadas indicadas por X y O")
    position_player = {'X' : [], 'O' : []} 

###Entender el diseño de Game-Loop de tres en raya Python
    while True:  
        tictactoe_grid(value)
#usando el bucle while para llamar a la función tictactoe_grid siempre que permanezca en VERDADERO.
        print(" Es tu turno!!! ")

        try:  
            print("El jugador ", player_current, " Ahora tienes que elegir tu bloque: ", end="")  
            chance = int(input())  
        except ValueError:  
            print("Este no es un valor valido!!! Por favor intenta de nuevo!")  
            continue
  
        print("")  
        if chance < 1 or chance > 9:  
            print("Este no es un valor permitido!! Por favor intenta de nuevo!")  
            continue  
   
        print(" ") 
        if value[chance - 1] != ' ':  
            print("¡Ups! El puesto ya está ocupado. ¡Inténtalo de nuevo!")  
            continue  


###Para actualizar las entradas de un jugador en la información del juego de tic tac toe Python

        value[chance - 1] = player_current  
#  Al agregar el código anterior, actualizamos el estado del tablero
 
        position_player[player_current].append(chance)  
# Al agregar el código anterior, actualizamos la posición del jugador en la cuadrícula.
 
#  llamando a la UDF para comprobar si hay ganador
        if win_validate(position_player, player_current):  
            tictactoe_grid(value)  
            print("LO LOGRASTE!!!", player_current, " ha ganado el juego !")       
            print("\n")  
            return player_current  
      
# llamando a la UDF en caso de empate 
        if tie_validate(position_player):  
            tictactoe_grid(value)  
            print("¡Estuvo cerca! El juego está empatado")  
            print("\n")  
            return 'D'  
 
###Para validar el cambio entre el jugador una vez que se ejecuta la oportunidad de un jugador
# usando el ciclo if-else en Python para hacer el cambio entre el reproductor 
        if player_current == 'X':  
            player_current = 'O'  
        else:  
            player_current = 'X'
    
    
###Registrar los nombres de los jugadores para observar en el marcador

if __name__ == "__main__":  
   
    print("   Nombre del jugador 1  ")  
    player_first = input("Por favor ingresa tu nombre: ")  
    print("\n")  
# implementar la función de entrada en Python para permitir que el usuario del juego ingrese su nombre

    print("   Nombre del jugador 2")  
    player_second = input("Por favor ingresa tu nombre:  ")  
    print("\n")
     
### Para capturar la información del juego
# Capturar al jugador que elige la X y la O
    player_current = player_first  
   
#  Capturando la elección de las jugadoras(femenino)
    player_choice = {'X' : "", 'O' : ""}  
   
# Almacenamiento de las dos posibles opciones disponibles para el juego Python de tres en raya
    option = ['X', 'O']  
   
# Almacenar la información que necesita ser capturada en el marcador
 
    score_board = {player_first: 0, player_second: 0}  
    my_scoreboard(score_board)  
 
###Para crear un bucle externo para hacer que nuestro juego sea flexible y permitir que se jueguen múltiples juegos de tic tac toe Python

# Usar la función while en Python para agregar múltiples series de juegos hasta que los jugadores lo llamen una salida.
    while True:  
# Menú mostrado a los jugadores
        print(player_current, ", tienes la oportunidad de elegir con la serie a jugar:")  
        print("Presiona 1 para X")  
        print("Presiona 2 para O")  
        print("Presiona 3 para salir") 
 
###Para manejar la excepción y asignar la selección del símbolo para el jugador actual para cada iteración del juego

#  El bloque try-except para la entrada the_choice del reproductor 
        try:  
            the_choice = int(input())     
        except ValueError:  
            print("This input is Invalid!!! Please Try Again\n")  
            continue  
   
#  repite en Python para definir la condición de la selección realizada  
        if the_choice == 1:  
            player_choice['X'] = player_current  
            if player_current == player_first:  
                player_choice['O'] = player_second  
            else:  
                player_choice['O'] = player_first  
   
        elif the_choice == 2:  
            player_choice['O'] = player_current  
            if player_current == player_first:  
                player_choice['X'] = player_second  
            else:  
                player_choice['X'] = player_first  
           
        elif the_choice == 3:
            print("\n")
            print("Gracias por jugar!!!")
            print("A continuacion  Los puntajes finales: ")  
            my_scoreboard(score_board)  
            break    
   
        else:  
            print("This is an Invalid choice!! Please try again\n") 
 
###Ejecución del juego Python tres en raya y actualización del marcador simultáneamente
# Capturando al ganador del juego individual de Tic-Tac-Toe Python

        winner = game_single(option[the_choice - 1]) 

# Según los puntajes obtenidos, el ganador se actualiza en el marcador.
        if winner != 'D' :  
            player_won = player_choice[winner]  
            score_board[player_won] = score_board[player_won] + 1 
 
            my_scoreboard(score_board)

 ###Intercambio de la oportunidad dada para elegir el símbolo entre el jugador seleccionador
# Cambiar entre los jugadores después de cada juego para elegir quién elegirá X u O
        if player_current == player_first:  
            player_current = player_second  
        else:  
            player_current = player_first 
