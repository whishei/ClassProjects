# Othello 
import numpy as np
from copy import deepcopy
from MCTS import * 
import ast

#Defining the Othello Class
class Othello():


    def __init__(self, board = None):
        # Initializing the game, creating needed global variables for printing, switching turns, position (current state of board). 

        self.length = 4

        self.player1 = 'x'
        self.player2 = 'o'
        self.empty = '.'
        self.player = 1
        self.winner = 0
        
        self.position = []
        self.is_Terminal = False

        self.init_board()

        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)       
            

    def init_board(self):
        # Initializing the board with the inital 4 pieces

        length = self.length
        self.position = np.full((length,length),'.')
        self.position[int(length/2) - 1][int(length/2) - 1] = self.player2
        self.position[int(length/2) - 1][int(length/2)] = self.player1
        self.position[int(length/2)][int(length/2) - 1] = self.player1
        self.position[int(length/2)][int(length/2)] = self.player2

    def print_board(self):
        # Printing the board in a pretty way

        board = self.position

        if self.length == 4:
        #For 4 length board
            print ('  | 1 | 2 | 3 | 4 |')
            print ('   ________________')
            print(" | \n".join(str(i + 1) + " | " + " | ".join(row) for i, row in enumerate(board)) + ' |')
            print ('   ----------------')

        if self.length == 6:
        #For 6 length board
            print ('  | 1 | 2 | 3 | 4 | 5 | 6 |')
            print ('   _______________________')
            print(" | \n".join(str(i + 1) + " | " + " | ".join(row) for i, row in enumerate(board)) + ' |')
            print ('   -----------------------')

        if self.length == 8:
        #For 8 length board
            print ('  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
            print ('   _______________________________')
            print(" | \n".join(str(i + 1) + " | " + " | ".join(row) for i, row in enumerate(board)) + ' |')
            print ('   -------------------------------')



    def to_skip(self):

        possible,direction  = self.find_potential_moves(self.player)
            
        if possible == []:
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            
            return True
        
        else:
            return False

    def find_potential_moves(self, player):
        # Finding all potential moves the current player could make on the current state of the board 

        board = self.position
        length = len(board)   

        if player == 1:
            check = self.player2
            check2 = self.player1
        else:
            check = self.player1
            check2 = self.player2

        potential = []
        directions = []
        for i in range(0,length):
            for j in range(0,length):

                if board[i][j] == '.':
                
                    #CHECK ABOVE
                    if i > 0:
                        if board[i-1][j] == check:
                            current_row = i-1
                            current_col = j 
                            while current_row > 0 and board[current_row][current_col] != self.empty:
                                current_row = current_row - 1
                                if board[current_row][current_col] == check2:
                                    directions.append('a')
                                    potential.append([i,j])
                    
                    #CHECK BELOW
                    if i < length - 1:
                        if board[i+1][j] == check:
                            current_row = i+1
                            current_col = j 
                            while current_row < length - 1 and board[current_row][current_col] != self.empty:
                                current_row = current_row + 1
                                if board[current_row][current_col] == check2:
                                    directions.append('b')
                                    potential.append([i,j])

                    #CHECK RIGHT
                    if j < length - 1:
                        if board[i][j+1] == check:
                            current_row = i
                            current_col = j + 1
                            while current_col < length - 1 and board[current_row][current_col] != self.empty:
                                current_col = current_col + 1
                                if board[current_row][current_col] == check2:
                                    directions.append('r')
                                    potential.append([i,j])

                    #CHECK LEFT 
                    if j > 0:
                        if board[i][j-1] == check:
                            current_row = i
                            current_col = j - 1
                            while current_col > 0 and board[current_row][current_col] != self.empty:
                                current_col = current_col - 1
                                if board[current_row][current_col] == check2:
                                    directions.append('l')
                                    potential.append([i,j])

                    #CHECK TOP RIGHT
                    if i > 0 and j < length - 1:
                        if board[i-1][j+1] == check:
                            current_row = i - 1
                            current_col = j + 1
                            while current_row > 0 and current_col < length - 1 and board[current_row][current_col] != self.empty:
                                current_row = current_row - 1
                                current_col = current_col + 1
                                if board[current_row][current_col] == check2:
                                    directions.append('ar')
                                    potential.append([i,j])

                    #CHECK BOTTOM RIGHT
                    if i < length - 1 and j < length - 1:
                        if board[i+1][j+1] == check:
                            current_row = i + 1
                            current_col = j + 1
                            while current_row < length - 1 and current_col < length - 1 and board[current_row][current_col] != self.empty:
                                current_row = current_row + 1
                                current_col = current_col + 1
                                if board[current_row][current_col] == check2:
                                    directions.append('br')
                                    potential.append([i,j])

                    #CHECK TOP LEFT
                    if i > 0 and j > 0:
                        if board[i-1][j-1] == check:
                            current_row = i - 1
                            current_col = j - 1
                            while current_row > 0 and current_col > 0 and board[current_row][current_col] != self.empty:
                                current_row = current_row - 1
                                current_col = current_col - 1
                                if board[current_row][current_col] == check2:
                                    directions.append('al')
                                    potential.append([i,j])

                    #CHECK BOTTOM LEFT
                    if i < length - 1 and j > 0:
                        if board[i+1][j-1] == check:
                            current_row = i + 1
                            current_col = j - 1
                            while current_row < length - 1 and current_col > 0 and board[current_row][current_col] != self.empty:
                                current_row = current_row + 1
                                current_col = current_col - 1
                                if board[current_row][current_col] == check2:
                                    directions.append('bl')
                                    potential.append([i,j])


        a = potential

        dicts = {}

        for i in range(0,len(a)):
            if str(a[i]) not in dicts:
                dicts[str(a[i])] =  [directions[i]]
            else:
                direct = dicts[str(a[i])]
                direct.append(directions[i])
                dicts[str(a[i])] = direct

        unique_a = list(dicts.keys())
        for i in range (0,len(unique_a)):
            unique_a[i] = ast.literal_eval(unique_a[i])
        unique_directions = list(dicts.values())
            
        return unique_a,unique_directions



    def make_move(self,row,col,neighbors):
        # Making a move on the board and flipping all needed symbols 

        board = Othello(self)

        length = len(board.position)

        if self.player == 1:
            check = self.player1
            board.player = 2
        else:
            check = self.player2
            board.player = 1


        found = False
        for i in neighbors:
            current_row = row
            current_col = col    

            #Looking Above
            if i == 'a':
                while current_row > 0 and found == False:
                    board.position[current_row][current_col] = check 
                    current_row = current_row - 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

            #Looking Below
            elif i == 'b':
                while current_row < length - 1 and found == False:
                    board.position[current_row][current_col] = check 
                    current_row = current_row + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

            #Looking Right
            elif i == 'r':
                while current_col < length - 1 and found == False:
                    board.position[current_row][current_col] = check 
                    current_col = current_col + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

            #Looking Left
            elif i == 'l':
                while current_col > 0 and found == False:
                    board.position[current_row][current_col] = check 
                    current_col = current_col - 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

            #Looking Top Right Diagonal 
            elif i == 'ar':
                while current_row > 0 and current_col < length - 1 and found == False: 
                    board.position[current_row][current_col] = check 
                    current_row = current_row - 1
                    current_col = current_col + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

            #Check top left diagonal  
            elif i == 'al':
                while current_row > 0 and current_col > 0 and found == False: 
                    board.position[current_row][current_col] = check 
                    current_row = current_row - 1
                    current_col = current_col - 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

            #Check bottom right diagonal 
            elif i == 'br':
                while current_row < length - 1 and current_col < length - 1 and found == False:
                    board.position[current_row][current_col] = check 
                    current_row = current_row + 1
                    current_col = current_col + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

            #Check bottom left diagonal  
            elif i == 'bl':
                while current_row < length - 1 and current_col > 0 and found == False:
                    board.position[current_row][current_col] = check 
                    current_row = current_row + 1
                    current_col = current_col - 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
                current_row = row
                current_col = col  

        return board
    

    def count_positions(self):
        # Counting current sums of players symbols on the board 

        board = self.position
        length = len(board)

        sum1 = 0
        sum2 = 0
        for i in range(0,length):
            for j in range(0,length):
                if board[i][j] == 'x':
                    sum1 = sum1 + 1
                else:
                    sum2 = sum2 + 1

        return sum1,sum2



    def is_win(self):
        # Defining what it means that the board is at a win

        if '.' not in self.position:
            sum1,sum2 = self.count_positions()
            if sum1 > sum2:
                self.is_Terminal = True
                self.winner = 1
                #print (" Yay you won! :) ")
                return True
            elif sum1 < sum2:
                self.is_Terminal = True
                self.winner = 2
                #print (" BOO the computer won! :( ")
                return True
        
        # NO MORE MOVES

        moves1,direction1 = self.find_potential_moves(1)
        moves2,direction2 = self.find_potential_moves(2)

        if moves1 == [] and moves2 == []:
            sum1,sum2 = self.count_positions()
            if sum1 > sum2:
                self.is_Terminal = True
                self.winner = 1
                #print (" Yay you won! :) ")
                return True
            elif sum1 < sum2:
                self.is_Terminal = True
                self.winner = 2
                #print (" BOO the computer won! :( ")
                return True
        
        return False

    
    def is_tie(self):
        # Defining what it means that the board is at a tie

        if '.' not in self.position: 
            sum1,sum2 = self.count_positions()
            if sum1 == sum2:
                self.is_Terminal = True
                #print ('TIE!')
                return True
        
        # NO MORE MOVES
        moves1,direction1 = self.find_potential_moves(1)
        moves2,direction2 = self.find_potential_moves(2)

        if moves1 == [] and moves2 == []:
            sum1,sum2 = self.count_positions()
            if sum1 == sum2:
                self.is_Terminal = True
                print ('TIE!')
                return True
        
        return False


    
    def generate_states(self):
        #Generating the states for MCTS

        self.to_skip()
        possible,directions  = self.find_potential_moves(self.player)

        actions = []

        #NEED TO CHANGE THIS FOR VALID MOVES ONLY
        for i in range(0,len(possible)):
            actions.append(self.make_move(possible[i][0],possible[i][1],directions[i]))

        return actions
    
    def is_valid(self,row,col):
        #Checking if the selected move is valid

        board = self.position

        #Can't go outside of board
        if row >= len(board) or col >= len(board) or row < 0 or col < 0:
            return False, []
        
        #Space is not empty
        elif board[row][col] != '.':
            return False, []
        
        moves, directions = self.find_potential_moves(self.player)

        #Getting the correct directions for the chosen move
        if [row,col] in moves:
            index = moves.index([row,col])
            return True, directions[index]
        
        else:
            return False, []
    

    def play_game(self):
        tree = MCTS()

        print(' Welcome to Othello! The goal of the game is to have more of your symbol (x) on the board than the computer (o). Good luck!')
        
        self.print_board()


        while self.is_Terminal == False:

            if self.player == 1:
                print ("It's your turn!")

                move = input("Please enter the row and column of your choice of move in the format: row,col ")
                try: 
                    row = int(move[0]) - 1
                    col = int(move[2]) - 1
                except IndexError:
                    move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                    row = int(move[0]) - 1 
                    col = int(move[2]) - 1

                valid,directions = self.is_valid(row,col)
                while valid == False:
                    move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                    try: 
                        row = int(move[0]) - 1 
                        col = int(move[2]) - 1
                    except IndexError:
                        pass

                    valid,directions = self.is_valid(row,col)

                self = self.make_move(row,col,directions)

                self.print_board()

                if self.to_skip() == True:
                    print ("Skipping turns")
                
                # check if the game is won
                if self.is_win():
                    if self.winner == 1:
                        print (" Yay you won! :) ")
                    else:
                        print (" BOO the computer won! :( ")
                    break
                elif self.is_tie():
                    break

            else: 

                print ("It's the computer's turn!")
            
                move = tree.search(self)

                try:
                    # make AI move here
                    self = move.board
                    
                # game over
                except:
                    pass

                self.print_board()

                if self.to_skip() == True:
                    print ("Skipping turns")
                    
                # check if the game is won
                if self.is_win():
                    if self.winner == 1:
                        print (" Yay you won! :) ")
                    else:
                        print (" BOO the computer won! :( ")
                    break
                elif self.is_tie():
                    break


if __name__ == '__main__':
    # create board instance
    play = Othello()
    
    # start game loop
    play.play_game()

#Need to fix allowed inputs - only single digit numbers and if anything else do invalid move. 
