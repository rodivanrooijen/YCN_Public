from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the Tic-Tac-Toe class and game logic here
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        
        if ' ' not in self.board:
            return 'Tie'
        
        return None

    def is_valid_move(self, position):
        return 0 <= position < 9 and self.board[position] == ' '

    def display_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    # ... (copy and paste the TicTacToe class and its methods here)

# Create a new Tic-Tac-Toe game
game = TicTacToe()

# Define the Flask routes below
@app.route('/')
def index():
    return render_template('index.html', board=game.board, current_player=game.current_player)

@app.route('/move/<int:position>', methods=['POST'])
def make_move(position):
    if game.is_valid_move(position):
        game.make_move(position)
        winner = game.check_winner()
        if winner:
            if winner == 'Tie':
                return "It's a tie!"
            else:
                return f"Player {winner} wins!"
        return redirect(url_for('index'))
    else:
        return "Invalid move. Try again."

if __name__ == '__main__':
    app.run(debug=True)

