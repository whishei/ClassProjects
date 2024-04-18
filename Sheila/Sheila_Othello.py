# Othello 
import numpy as np
from Sheila_MCTS import * 

class Othello:
    def __init__(self):

        length = 4

        self.board = np.full((length,length),0)
        self.board[int(length/2) - 1][int(length/2) - 1] = 1
        self.board[int(length/2) - 1][int(length/2)] = -1
        self.board[int(length/2)][int(length/2) - 1] = -1
        self.board[int(length/2)][int(length/2)] = 1

        self.player1 = 'x'
        self.player2 = 'o'
        self.empty = '.'
        self.player = 1
        
        self.position = -1
        self.is_Terminal = False

    def make_move(self,row,col):

        board = self.board

        if self.player == 1:
            board[row,col] = 1
            self.player = -1
        else:
            board[row,col] = -1
            self.player = 1

    def print_board(self):
        board = self.board
        length = len(board)

        pretty = np.full((length,length),'.')
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == 1:
                    pretty[i][j] = self.player1
                elif board[i][j] == -1:
                   pretty[i][j] = self.player2

        # print ('\t1\t2\t3\t4') #\t5\t6\t7\t8')
        # print("\n".join(str(i + 1) + "\t" +"\t".join(row) for i, row in enumerate(pretty)))

        print ('\t0\t1\t2\t3') #\t5\t6\t7\t8')
        print("\n".join(str(i) + "\t" +"\t".join(row) for i, row in enumerate(pretty)))


    def isValid(self,row,col):
        board = self.board

        #Can't go outside of board
        if row >= len(board) or col >= len(board) or row < 0 or col < 0:
            return False
        
        #Space is not empty
        elif board[row][col] != 0:
            return False
        
        neighbors = []
        directions = []
        #Check above
        if row - 1 >= 0:
            if board[row - 1][col] == -self.player:
                neighbors.append([row-1,col])
                directions.append('a')
                print ('ABOVE')
        #Check below
        if row + 1 <= len(board)-1:
            if board[row + 1][col] == -self.player:
                neighbors.append([row+1,col])
                directions.append('b')
                print ("BELOW")
        #Check left
        if col - 1 >= 0:
            if board[row][col-1] == -self.player:
                neighbors.append([row,col-1])
                directions.append('l')
                print ("LEFT")
        #Check right
        if col + 1 <= len(board)-1:
            if board[row][col + 1] == -self.player:
                neighbors.append([row,col + 1])
                directions.append('r')
                print ("RIGHT")
        #Check top right diagonal 
        if row - 1 >= 0 and col + 1 <= len(board) - 1:
            if board[row - 1][col + 1] == -self.player:
                neighbors.append([row - 1,col + 1])
                directions.append('ar')
                print ("TOP RIGHT Diagonal")
        #Check top left diagonal  
        if row - 1 >= 0 and col - 1 >= 0:
            if board[row - 1][col - 1] == -self.player:
                neighbors.append([row - 1,col - 1])
                directions.append('al')
                print ("TOP LEFT Diagonal")
        #Check bottom right diagonal 
        if row + 1 <= len(board) - 1 and col + 1 <= len(board) - 1:
            if board[row + 1][col + 1] == -self.player:
                neighbors.append([row + 1,col + 1])
                directions.append('br')
                print ("BOTTOM RIGHT Diagonal")
        #Check bottom left diagonal  
        if row + 1 <= len(board) - 1 and col - 1 >= 0:
            if board[row + 1][col - 1] == -self.player:
                neighbors.append([row + 1,col - 1])
                directions.append('bl')
                print ("BOTTOM LEFT Diagonal")

        #print (neighbors)
        if neighbors == []:
            return False

        found = False
        choices = []
        for i in range(0,len(neighbors)):
            while found != True:
                current_row = neighbors[i][0]
                current_col = neighbors[i][1]    
                if directions[i] == 'a':
                   while current_row >= 0:
                       current_row = current_row - 1
                       if board[current_row][current_col] == self.player:
                           found = True
                           #choices.append(board[current_row][current_col])
                elif directions[i] == 'b':
                   while current_row <= len(board) - 1:
                       current_row = current_row + 1
                       if board[current_row][current_col] == self.player:
                           found = True
                           #choices.append(board[current_row][current_col])
                elif directions[i] == 'r':
                   while current_col <= len(board) - 1:
                       current_col = current_col + 1
                       if board[current_row][current_col] == self.player:
                           found = True
                           #choices.append(board[current_row][current_col])
                elif directions[i] == 'l':
                   while current_col >= 0:
                       current_col = current_col - 1
                       if board[current_row][current_col] == self.player:
                           found = True
                           #choices.append(board[current_row][current_col])
                elif directions[i] == 'ar':
                   while current_row <= len(board) - 1:
                       current_row = current_row + 1

                       row - 1 >= 0 and col + 1 <= len(board) - 1:
                       if board[current_row][current_col] == self.player:
                           found = True
                           #choices.append(board[current_row][current_col])

            
 ####NEED TO CHECK THESE STEPS 

    


        return True

        

    def possibleMoves(self):
        board = self.board
        player = self.player

        #if player == 1:


    
    def end_Game(self):
        if 0 not in self.board:
            self.is_Terminal = True
        

def play_game():
    tree = MCTS()
    game = Othello()
    game.print_board()

    i = 0
    while game.is_Terminal == False:
        move = input("Please enter the row and column of your choice of move in the format: row,col ")
        try: 
            row = int(move[0]) - 1
            col = int(move[2]) - 1
        except IndexError:
            move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
            row = int(move[0]) - 1 
            col = int(move[2]) - 1
        while game.isValid(row,col) == False:
            move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
            try: 
                row = int(move[0]) - 1 
                col = int(move[2]) - 1
            except IndexError:
                pass

        game.make_move(row,col)

        # if i == 4:
        #     game.is_Terminal = True

        game.print_board()

        game.end_Game()
        i = i + 1

play_game()


#Need to fix allowed inputs - only single digit numbers and if anything else do invalid move. 