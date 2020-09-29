#tic_tac_toe.py
#Date: 29/September/2020
#by irving-rs

#Description:
#Tic-tac-toe: The classical game played on a 3x3 grid.

#Basics:
#The player always starts the game doing the first move.
#The computer (oponnent) selects a random move.
#The first one that forms a line of three wins.


#IMPORTING MODULES:
from random import randrange

#FUNCTIONS:
def dibuja(tablero): #Draws the board.
    print("\n\t-------------")
    print("\t|", tablero[0][0], "|", tablero[0][1], "|", tablero[0][2], "|")
    print("\t-------------")
    print("\t|", tablero[1][0], "|", tablero[1][1], "|", tablero[1][2], "|")
    print("\t-------------")
    print("\t|", tablero[2][0], "|", tablero[2][1], "|", tablero[2][2], "|")
    print("\t-------------\n")

def validaFormato(sel): #Verifies that the number format is correct. Returns Tue or False.
    if sel<1 or sel>9:
        print("\nInvalid format, try again.\n")
        return False
    else:
        return True

def disponible(sel): #Checs if the space is available.
    global libre
    x = dic[sel]
    if x in libre:
        for i in range(len(libre)):
            if x==libre[i]:
                del libre[i]
                break
        return True
    else:
        print("\nThe selected space is not available. Try again.\n")
        return False

def maquina(): #Aleatory movement.
    global tablero
    global libre
    x = randrange(len(libre))
    tablero[libre[x][0]][libre[x][1]] = "O"
    del libre[x]

def ganador(tablero, s): #Verifies if there is a winner.
    #Horizontal line 1:
    if tablero[0][0]==s and tablero[0][1]==s and tablero[0][2]==s:
        return True
    #Horizontal line 2:
    elif tablero[1][0]==s and tablero[1][1]==s and tablero[1][2]==s:
        return True
    #Horizontal line 3:
    elif tablero[2][0]==s and tablero[2][1]==s and tablero[2][2]==s:
        return True
    #Vertical line 1:
    elif tablero[0][0]==s and tablero[1][0]==s and tablero[2][0]==s:
        return True
    #Vertical line 2:
    elif tablero[0][1]==s and tablero[1][1]==s and tablero[2][1]==s:
        return True
    #Vertical line 3:
    elif tablero[0][2]==s and tablero[1][2]==s and tablero[2][2]==s:
        return True
    #Diagonal line 1:
    elif tablero[0][0]==s and tablero[1][1]==s and tablero[2][2]==s:
        return True
    #Diagonal line 2:
    elif tablero[2][0]==s and tablero[1][1]==s and tablero[0][2]==s:
        return True
    else:
        return False

#VARIABLES AND CONSTANTS:
tablero = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] #Stores the state of the board.
dic = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)} #Dictionary.
libre = [ (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) ] #Stores a tuple of the position where free spaces are.

#PRESENTATION OF THE GAME:
print("\nTic-tac-toe")

#BODY:

dibuja(tablero) #Draws the board.

while True:

    if len(libre)==0: #If there are not free spaces on the board.
        print("Draw.")
        break
    
    #Users turn:
    sel = int(input("Select the number where you want to make your move: "))
    if validaFormato(sel)==True and disponible(sel)==True: #If the space is available and the format is valid.
        tablero[dic[sel][0]][dic[sel][1]] = "X" #Users choice.
        dibuja(tablero) #Draws the board.
    else:
        continue
    if ganador(tablero, "X")==True:
        print("¡You have won!\n")
        break
    
    if len(libre)==0: #If there are not available spaces, then the game finishes.
        print("Draw.")
        break

    #Computers turn:
    maquina()
    print("The computer has made its move: ")
    dibuja(tablero) #Draws the board.
    if ganador(tablero, "O")==True:
        print("¡You have lost!\n")
        break
