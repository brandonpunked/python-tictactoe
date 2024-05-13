import random

# Tic Tac Toe 

def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    isFull(board, symbol_1, symbol_2)
    

    


def intro():
    # Introduces the game of Tic Tac Toe
    print("Tic Tac Toe for Mr. Bradpitt")
    print("\n")
    print("Rules: You (Player) will play against an AI (Computer). You are represented by X, and the AI is represented by O. Take turns "
          "marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")



def create_grid():
    # Playboard created
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board



def sym():
    # Players symbols decided
    symbol_1 = input("Do you want to be X or O? ")
    if symbol_1.upper() == "X":
        symbol_2 = "O"
        print("You are X. The AI is O.")
    else:
        symbol_2 = "X"
        print("You are O. The AI is X.")
    input("Press enter to continue.")
    print("\n")
    return (symbol_1.upper(), symbol_2)



def startGamming(board, symbol_1, symbol_2, count):
    # Starts the game.

    # Decides the turn
    if count % 2 == 0:
        player = symbol_1
        print("Your turn.")
        row = int(input("Pick a row:"
                        "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

        # Check if players' selected spot is out of range
        while (row > 2 or row < 0) or (column > 2 or column < 0):
            outOfBoard(row, column)
            row = int(input("Pick a row[upper row:"
                            "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
            column = int(input("Pick a column:"
                               "[left column: enter 0, middle column: enter 1, right column enter 2]"))

        # Check if square is already filled
        while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
            filled = illegal(board, symbol_1, symbol_2, row, column)
            row = int(input("Pick a row[upper row:"
                            "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
            column = int(input("Pick a column:"
                                "[left column: enter 0, middle column: enter 1, right column enter 2]"))    
        
        # Locates player's place on the board
        board[row][column] = symbol_1
            
    else:
        player = symbol_2
        print("AI's turn.")
        # AI making a move
        row, column = ai_move(board, symbol_1, symbol_2)
        print(f"AI chooses row {row} and column {column}.")
        board[row][column] = symbol_2
    
    return (board)



def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = None
    # Check if board is full
    while count < 10 and winner is None:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
        
        # Winner decided
        winner = isWinner(board, symbol_1, symbol_2)
        if winner == symbol_1: # Player wins
            print("Congratulations! You won!")
            print("HOW THE INTERNET WORKS IN VIDEO GAME TERMS:\n"
                  "Player Interaction: Like players connecting to a gaming server, devices connect to the Internet to interact with servers and other devices\n"
                  "Data Transmission: Game actions are sent to servers like data packets travel across the Internet through routers and switches.\n"
                  "Protocols and Security: Games use protocols for communication and implement security measures like the Internet relies on protocols and security measures to ensure smooth and secure data transmission.")
            print("Also, fun fact: The OSI model is a seven layers that computer systems use to communicate over a network. Here is it explained in video game terms\n"
                  "Application Layer: The game itself, where players interact and exchange data.\n"
                  "Presentation Layer: Rendering of graphics and conversion of player actions into data packets.\n"
                  "Session Layer: Connections between players, handling session initiation, maintenance, and termination.\n"
                  "Transport Layer: Data packets are delivered reliably and in the correct order between players and servers.\n"
                  "Network Layer: Routing data packets between players and servers, determining the best path for transmission.\n"
                  "Data Link Layer: Transmission of data packets over the physical medium, such as Ethernet or Wi-Fi.\n"
                  "Physical Layer: Actual hardware components used for data transmission, such as network interface cards and cables.")
            break
        elif winner == symbol_2: # AI wins
            print("AI wins!")
            break
        elif count == 9: # Game ends in a tie
            print("The board is full. Game over.")
            print("Game tied.")
            break
        count += 1
    print("Game over.")
        


def outOfBoard(row, column):
    # Lets player know if they are out of range
    print("Out of the playing board. Pick another one. ")
    
    

def printPretty(board):
    # The board print
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board



def isWinner(board, symbol_1, symbol_2):
    # Checks if any winner is winning
    # Checks the rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            return symbol_1
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            return symbol_2
            
    # Checks the columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            return symbol_1
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            return symbol_2

    # Checks the diagonals
    if (board[0][0] == board[1][1] == board[2][2] == symbol_1) or (board[0][2] == board[1][1] == board[2][0] == symbol_1):
        return symbol_1
    elif (board[0][0] == board[1][1] == board[2][2] == symbol_2) or (board[0][2] == board[1][1] == board[2][0] == symbol_2):
        return symbol_2

    return None
    


def illegal(board, symbol_1, symbol_2, row, column):
    # Player notified that the square they picked is filled. 
    print("The square you picked is already filled. Pick another one.")

def ai_move(board, symbol_1, symbol_2):
    # Implement the AI moving
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None, None
    
# Call Main
main()