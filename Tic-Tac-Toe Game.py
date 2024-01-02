# Tic-Tac-Toe Game

# Define the board
board = [' ']*9

# Define the function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Define the function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if all([board[j] == player for j in range(i, i+3)]):
            return True
    # Check columns
    for i in range(3):
        if all([board[j] == player for j in range(i, 9, 3)]):
            return True
    # Check diagonals
    if all([board[i] == player for i in range(0, 9, 4)]) or all([board[i] == player for i in range(2, 7, 2)]):
        return True
    # No win condition found
    return False

# Define the main game loop
def play_game():
    # Initialize the player
    player = 'X'
    # Loop until the game is over
    while True:
        # Print the board
        print_board()
        # Get the player's move
        print('Player', player, 'move:')
        position = int(input('Enter a position (1-9): ')) - 1
        # Check if the move is valid
        if board[position] != ' ':
            print('Invalid move, try again.')
            continue
        # Make the move
        board[position] = player
        # Check if the player has won
        if check_win(player):
            print_board()
            print('Player', player, 'wins!')
            break
        # Check if the game is a tie
        if all([cell != ' ' for cell in board]):
            print_board()
            print('Game over, tie!')
            break
        # Switch to the other player
        player = 'O' if player == 'X' else 'X'

# Start the game
play_game()