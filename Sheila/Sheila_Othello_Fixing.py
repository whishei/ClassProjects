# Othello 
import numpy as np
from copy import deepcopy
from Sheila_MCTS_Fixing import * 

class Othello():
    def __init__(self, board = None):

        self.length = 4

        self.player1 = 'x'
        self.player2 = 'o'
        self.empty = '.'
        self.player = 1
        
        self.position = []
        self.is_Terminal = False

        self.init_board()

        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)       
            

    def init_board(self):

        length = self.length
        self.position = np.full((length,length),0)
        self.position[int(length/2) - 1][int(length/2) - 1] = 1
        self.position[int(length/2) - 1][int(length/2)] = -1
        self.position[int(length/2)][int(length/2) - 1] = -1
        self.position[int(length/2)][int(length/2)] = 1

    def make_move(self,row,col):

        board = Othello(self)

        if self.player == 1:
            board.position[row,col] = self.player1
            self.player = 2
        else:
            board.position[row,col] = self.player2
            self.player = 1

    def is_Win(self):

        if '.' not in self.position:
            sum1 = sum(row.count(self.player1) for row in self.position)
            sum2 = sum(row.count(self.player2) for row in self.position)
            if sum1 != sum2:
                self.is_Terminal = True
                return True
        
        # NO MORE MOVES


        return False
    
    def is_Tie(self):
        if '.' not in self.position and self.is_Win() == False:
            sum1 = sum(row.count(self.player1) for row in self.position)
            sum2 = sum(row.count(self.player2) for row in self.position)
            if sum1 == sum2:
                self.is_Terminal = True
                return True
        
        # NO MORE MOVES

        return False
    
    def generate_states(self):

        actions = []

        #NEED TO CHANGE THIS FOR VALID MOVES ONLY

        for row in range(0, len(self.position)):
            for col in range(0, len(self.position[row])):
                if self.position[row][col] == self.empty:
                    actions.append(self.make_move(row,col))

        return actions
    
    def print_board(self):
        board = self.position
        print ('\t1\t2\t3')
        print("\n".join(str(i + 1) + "\t" +"\t".join(row) for i, row in enumerate(board)))


    # def print_board(self):
    #     board = self.board
    #     length = len(board)

    #     pretty = np.full((length,length),'.')
    #     for i in range(0,len(board)):
    #         for j in range(0,len(board[i])):
    #             if board[i][j] == 1:
    #                 pretty[i][j] = self.player1
    #             elif board[i][j] == -1:
    #                pretty[i][j] = self.player2

    #     # print ('\t1\t2\t3\t4') #\t5\t6\t7\t8')
    #     # print("\n".join(str(i + 1) + "\t" +"\t".join(row) for i, row in enumerate(pretty)))

    #     print ('\t0\t1\t2\t3') #\t5\t6\t7\t8')
    #     print("\n".join(str(i) + "\t" +"\t".join(row) for i, row in enumerate(pretty)))



        ##MOST IMPORTANT FUNCTION!!!
#     def isValid(self,row,col):
#         board = self.board

#         #Can't go outside of board
#         if row >= len(board) or col >= len(board) or row < 0 or col < 0:
#             return False
        
#         #Space is not empty
#         elif board[row][col] != 0:
#             return False
        
#         neighbors = []
#         directions = []
#         #Check above
#         if row - 1 >= 0:
#             if board[row - 1][col] == -self.player:
#                 neighbors.append([row-1,col])
#                 directions.append('a')
#                 print ('ABOVE')
#         #Check below
#         if row + 1 <= len(board)-1:
#             if board[row + 1][col] == -self.player:
#                 neighbors.append([row+1,col])
#                 directions.append('b')
#                 print ("BELOW")
#         #Check left
#         if col - 1 >= 0:
#             if board[row][col-1] == -self.player:
#                 neighbors.append([row,col-1])
#                 directions.append('l')
#                 print ("LEFT")
#         #Check right
#         if col + 1 <= len(board)-1:
#             if board[row][col + 1] == -self.player:
#                 neighbors.append([row,col + 1])
#                 directions.append('r')
#                 print ("RIGHT")
#         #Check top right diagonal 
#         if row - 1 >= 0 and col + 1 <= len(board) - 1:
#             if board[row - 1][col + 1] == -self.player:
#                 neighbors.append([row - 1,col + 1])
#                 directions.append('ar')
#                 print ("TOP RIGHT Diagonal")
#         #Check top left diagonal  
#         if row - 1 >= 0 and col - 1 >= 0:
#             if board[row - 1][col - 1] == -self.player:
#                 neighbors.append([row - 1,col - 1])
#                 directions.append('al')
#                 print ("TOP LEFT Diagonal")
#         #Check bottom right diagonal 
#         if row + 1 <= len(board) - 1 and col + 1 <= len(board) - 1:
#             if board[row + 1][col + 1] == -self.player:
#                 neighbors.append([row + 1,col + 1])
#                 directions.append('br')
#                 print ("BOTTOM RIGHT Diagonal")
#         #Check bottom left diagonal  
#         if row + 1 <= len(board) - 1 and col - 1 >= 0:
#             if board[row + 1][col - 1] == -self.player:
#                 neighbors.append([row + 1,col - 1])
#                 directions.append('bl')
#                 print ("BOTTOM LEFT Diagonal")

#         #print (neighbors)
#         if neighbors == []:
#             return False

#         found = False
#         choices = []
#         for i in range(0,len(neighbors)):
#             while found != True:
#                 current_row = neighbors[i][0]
#                 current_col = neighbors[i][1]    
#                 if directions[i] == 'a':
#                    while current_row >= 0:
#                        current_row = current_row - 1
#                        if board[current_row][current_col] == self.player:
#                            found = True
#                            #choices.append(board[current_row][current_col])
#                 elif directions[i] == 'b':
#                    while current_row <= len(board) - 1:
#                        current_row = current_row + 1
#                        if board[current_row][current_col] == self.player:
#                            found = True
#                            #choices.append(board[current_row][current_col])
#                 elif directions[i] == 'r':
#                    while current_col <= len(board) - 1:
#                        current_col = current_col + 1
#                        if board[current_row][current_col] == self.player:
#                            found = True
#                            #choices.append(board[current_row][current_col])
#                 elif directions[i] == 'l':
#                    while current_col >= 0:
#                        current_col = current_col - 1
#                        if board[current_row][current_col] == self.player:
#                            found = True
#                            #choices.append(board[current_row][current_col])
#                 elif directions[i] == 'ar':
#                    while current_row <= len(board) - 1:
#                        current_row = current_row + 1

#                        row - 1 >= 0 and col + 1 <= len(board) - 1:
#                        if board[current_row][current_col] == self.player:
#                            found = True
#                            #choices.append(board[current_row][current_col])

            
#  ####NEED TO CHECK THESE STEPS 

    


#         return True


    def play_game(self):
        tree = MCTS()
        
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

            self.make_move(row,col)

            # if i == 4:
            #     game.is_Terminal = True

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

if __name__ == '__main__':
    # create board instance
    play = Othello()
    
    # start game loop
    play.play_game()

#Need to fix allowed inputs - only single digit numbers and if anything else do invalid move. 