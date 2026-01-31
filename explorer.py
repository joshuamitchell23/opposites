board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = "X"
game_over = False
count = 0
def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
while game_over == False:
    show_board()
    print("It is your turn," + turn + ". Move to which place? (1-9)")
    move = input()
    move = int(move) - 1
    if board[move] == " ":
        board[move] = turn
        count = count + 1
    else:
        print("That place is already filled. Try again.")
        continue
    if board[0] == board[1] == board[2] and board[0] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    elif board[3] == board[4] == board[5] and board[3] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    elif board[6] == board[7] == board[8] and board[6] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    elif board[0] == board[3] == board[6] and board[0] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    elif board[1] == board[4] == board[7] and board[1] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    elif board[2] == board[5] == board[8] and board[2] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    elif board[0] == board[4] == board[8] and board[0] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    elif board[2] == board[4] == board[6] and board[2] != " ":
        show_board()
        print("Game Over! " + turn + " won.")
        break
    if count == 9:
        show_board()
        print("It's a Tie!")
        break
    if turn == "X":turn = "O"
    else:turn = "X"
