import numpy as np
from copy import deepcopy
from MCTS import *


#Defining the TicTacToe Class
class TicTacToe():


    def __init__(self, board = None):
        # Initializing the game, creating needed global variables for printing, switching turns, position (current state of board). 

        self.player1 = 'x' 
        self.player2 = 'o'
        self.empty = '.'
        self.is_Terminal = False

        self.player = 1
        self.position = []

        self.init_board()

        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)       
            
        
    def init_board(self):
        # Initializing the board itself as empty. 

        self.position = np.full((3,3),self.empty)
        

    def make_move(self, row, col):
        # Making the provided move on the board 

        board = TicTacToe(self)

        if self.player == 1:
            board.position[row,col] = self.player1
            board.player = 2
        else:
            board.position[row,col] = self.player2
            board.player = 1
        
        return board
    

    def is_win(self):
        # Checking if the current state of the board is a win 

        #Checking rows
        for i in range(0,len(self.position)):
            if self.position[i][0] == self.position[i][1] == self.position[i][2] != '.':
                self.is_Terminal = True
                return True
                
        #Checking columns
        for j in range(0,len(self.position[i])):
            if self.position[0][j] == self.position[1][j] == self.position[2][j] != '.':
                self.is_Terminal = True
                return True

        # Checking diagonals
        if self.position[0][0] == self.position[1][1] == self.position[2][2] != '.':
            self.is_Terminal = True
            return True
            
        if self.position[0][2] == self.position[1][1] == self.position[2][0] != '.':
            self.is_Terminal = True
            return True
        
        return False


    def is_tie(self):
        # Checking if the current state of the board is a tie

        if '.' not in self.position and self.is_win() == False:
            self.is_Terminal = True
            return True
        else:
            return False


    def generate_states(self):
        # Creating a list of states (children from current node) of possible moves that can be played next. 

        actions = []

        for row in range(0, len(self.position)):
            for col in range(0, len(self.position[row])):
                if self.position[row][col] == self.empty:
                    actions.append(self.make_move(row,col))

        return actions




    def print_board(self):
        # Printing the board in a pretty way

        board = self.position

        print ('  | 1 | 2 | 3 |')
        print ('   ___________')
        print(" | \n".join(str(i + 1) + " | " + " | ".join(row) for i, row in enumerate(board)) + ' |')
        print ('   -----------')

    def is_valid(self,row,col):
        # Checking if the move the user chose to do is a valid move (empty & on the board)

        board = self.position

        if row >= len(board) or col >= len(board) or row < 0 or col < 0:
            return False
        elif board[row][col] != '.':
            return False
        else:
            return True

    def play_game(self):
        # Actually playing the game!

        tree = MCTS()

        print(' Welcome to Tic-Tac-Toe! You will be playing first as x and the computer will be playing second as o. Good luck!')
        
        self.print_board()

        while self.is_Terminal == False:
            print ("It's your turn!")
            move = input("Please enter the row and column of your choice of move in the format: row,col ")
            try: 
                row = int(move[0]) - 1
                col = int(move[2]) - 1
            except IndexError:
                move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                row = int(move[0]) - 1 
                col = int(move[2]) - 1
            while self.is_valid(row,col) == False:
                move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                try: 
                    row = int(move[0]) - 1 
                    col = int(move[2]) - 1
                except IndexError:
                    pass

            self = self.make_move(row,col)

            self.print_board()

            # check if the game is won
            if self.is_win():
                if self.player == 1:
                    print('The computer won :(')
                else:
                    print('Yay! You won :)')
                break
            
            # check if the game is drawn
            elif self.is_tie():
                print('TIE')
                break

            print ("It's the computer's turn!")
            move = tree.search(self)

            try:
                # make AI move here
                self = move.board
                
            # game over
            except:
                pass

            self.print_board()


            # check if the game is won
            if self.is_win():
                if self.player == 1:
                    print('The computer won :(')
                else:
                    print('Yay! You won :)')
                break
            
            # check if the game is drawn
            elif self.is_tie():
                print('TIE')
                break



if __name__ == '__main__':
    # create board instance
    play = TicTacToe()
    
    # start game loop
    play.play_game()
