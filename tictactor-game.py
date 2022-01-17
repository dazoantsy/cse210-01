def main ():
    current_player = "x"
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    display (board)
    while not (winning(board) or draw(board)):
        board= move (current_player, board)
        display (board)
        current_player = turn (current_player)
    print ('You win!!!')
    print ('Good game. Thanks for playing!')
    
def display (board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()    

def move (player, board):
    move = input (f"It's {player}'s turn to choose a square (1-9): ")
    board[int(move)-1] = player
    return board

def turn (player):
    if player == "o":
        return "x"
    elif player == "x":
        return "o"

def draw(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True 
    
def winning(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


if __name__ == "__main__":
    main()