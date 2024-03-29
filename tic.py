#GLOBAL VAR
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

game_still_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

    #dispaly
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()
        #flip
        flip_player()

        #ended gameover
        if winner == "X" or winner =="O":
            print(winner + " won..")
        elif winner == None:
            print("Tie.")

def handle_turn(player):
    position = input("Chose a postion from space 1-9: ")
    position = int(position)- 1

    board[position] = player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner

    row_winner = check_rows()
    columns_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

        return

    return

def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
        
    elif row2:
        return board[3]
        
    elif row3:
        return board[6]
        1
    return
    return

def check_columns():
    global game_still_going

    column1 = board[0] == board[1] == board[2] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
        print("Winner")
    elif column2:
        return board[1]
        print("Winner")
    elif column3:
        return board[2]
        print("Winner")
    return

def check_diagonals():
    global game_still_going

    diagonal1 = board[0] == board[1] == board[2] != "-"
    diagonal2 = board[1] == board[4] == board[7] != "-"

    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
        print("winner")
    elif diagonal2:
        return board[6]
        print("Winner")
    return
    return

def check_if_tie():
    return

def flip_player():
    #Global
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()