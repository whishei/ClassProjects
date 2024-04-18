import numpy as np
from copy import deepcopy
from Sheila_MCTS import *

class TicTacToe():
    def __init__(self, board = None):
       
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
        self.position = np.full((3,3),self.empty)
        

    def make_move(self, row, col):

        board = TicTacToe(self)

        if self.player == 1:
            board.position[row,col] = self.player1
            board.player = 2
        else:
            board.position[row,col] = self.player2
            board.player = 1
        
        return board
    

    def is_Win(self):

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


    def is_Tie(self):
        if '.' not in self.position and self.is_Win() == False:
            self.is_Terminal = True
            return True
        else:
            return False


    def generate_states(self):

        actions = []

        for row in range(0, len(self.position)):
            for col in range(0, len(self.position[row])):
                if self.position[row][col] == self.empty:
                    actions.append(self.make_move(row,col))

        return actions




    def print_board(self):
        board = self.position
        print ('\t1\t2\t3')
        print("\n".join(str(i + 1) + "\t" +"\t".join(row) for i, row in enumerate(board)))

    def isValid(self,row,col):
        board = self.position

        if row >= len(board) or col >= len(board) or row < 0 or col < 0:
            return False
        elif board[row][col] != '.':
            return False
        else:
            return True
    
    # def end_Game(self):

    #     # win = False
    #     # tie = False
    #     # loss = False
    #     #Checking rows
    #     for i in range(0,len(self.board)):
    #         if self.board[i][0] == self.board[i][1] == self.board[i][2] != '.':
    #             self.is_Terminal = True
    #             if self.board[i][0] == 'x':
    #                 print ("You won :p ")
    #             else:
    #                print ("The computer won :( ")

    #     #Checking columns
    #     for j in range(0,len(self.board[i])):
    #         if self.board[0][j] == self.board[1][j] == self.board[2][j] != '.':
    #             self.is_Terminal = True
    #             if self.board[0][j] == 'x':
    #                 print("You won :p ")
    #             else:
    #                 print ("The computer won :( ")

    #     # Checking diagonals
    #     if self.board[0][0] == self.board[1][1] == self.board[2][2] != '.':
    #         self.is_Terminal = True
    #         if self.board[0][0] == 'x':
    #             print("You won :p ")
    #         else:
    #             print("The computer won :( ")
            
    #     if self.board[0][2] == self.board[1][1] == self.board[2][0] != '.':
    #         self.is_Terminal = True
    #         if self.board[i][0] == 'x':
    #             print("You won :p ")
    #         else:
    #            print ("The computer won :( ")

    #     # Tie
    #     if '.' not in self.board:
    #         self.is_Terminal = True
    
    #     return self.is_Terminal
        
    

    def play_game(self):
        tree = MCTS()
        #game = TicTacToe()
        self.print_board()

        while self.is_Terminal == False:
            move = input("Please enter the row and column of your choice of move in the format: row,col ")
            try: 
                row = int(move[0]) - 1
                col = int(move[2]) - 1
            except IndexError:
                move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                row = int(move[0]) - 1 
                col = int(move[2]) - 1
            while self.isValid(row,col) == False:
                move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                try: 
                    row = int(move[0]) - 1 
                    col = int(move[2]) - 1
                except IndexError:
                    pass

            self = self.make_move(row,col)

            self.print_board()

            # check if the game is won
            if self.is_Win():
                if self.player == 1:
                    print('The computer won :(')
                else:
                    print('Yay! You won :)')
                break
            
            # check if the game is drawn
            elif self.is_Tie():
                print('TIE')
                break

            #self.end_Game()

            move = tree.search(self)

            try:
                # make AI move here
                self = move.board
                
            # game over
            except:
                pass

            self.print_board()


            # check if the game is won
            if self.is_Win():
                if self.player == 1:
                    print('The computer won :(')
                else:
                    print('Yay! You won :)')
                break
            
            # check if the game is drawn
            elif self.is_Tie():
                print('TIE')
                break
            #game.make_move(move)

            #game.print_board()

            #game.end_Game()


if __name__ == '__main__':
    # create board instance
    play = TicTacToe()
    
    # start game loop
    play.play_game()


#Need to fix allowed inputs - only single digit numbers and if anything else do invalid move. 