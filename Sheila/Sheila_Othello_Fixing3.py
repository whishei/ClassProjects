# Othello 
import numpy as np
from copy import deepcopy
from Sheila_MCTS import * 
import ast

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
        self.position = np.full((length,length),'.')
        self.position[int(length/2) - 1][int(length/2) - 1] = 'x'
        self.position[int(length/2) - 1][int(length/2)] = 'o'
        self.position[int(length/2)][int(length/2) - 1] = 'o'
        self.position[int(length/2)][int(length/2)] = 'x'


    def unique_values_with_directions(self, a, directions):

        dicts = {}

        for i in range(0,len(a)):
            if str(a[i]) not in dicts:
                #unique_directions[0] = directions
                dicts[str(a[i])] =  [directions[i]]
            else:
                direct = dicts[str(a[i])]
                direct.append(directions[i])
                dicts[str(a[i])] = direct
        
        #print (dicts)

        unique_a = list(dicts.keys())
        for i in range (0,len(unique_a)):
            unique_a[i] = ast.literal_eval(unique_a[i])
        unique_directions = list(dicts.values())

        return unique_a, unique_directions


    def find_potential_moves(self, player):
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
                    if i != 0:
                        if board[i-1][j] == check:
                            potential.append([i,j])
                            directions.append('a')
                    
                    #CHECK BELOW
                    if i != length - 1:
                        if board[i+1][j] == check:
                            potential.append([i,j])
                            directions.append('b')

                    #CHECK RIGHT
                    if j != length - 1:
                        if board[i][j+1] == check:
                            potential.append([i,j])
                            directions.append('r')

                    #CHECK LEFT 
                    if j != 0:
                        if board[i][j-1] == check:
                            potential.append([i,j])
                            directions.append('l')

                    #CHECK TOP RIGHT
                    if i != 0 and j!= length - 1:
                        if board[i-1][j+1] == check:
                            potential.append([i,j])
                            directions.append('ar')

                    #CHECK BOTTOM RIGHT
                    if i != length - 1 and j!= length - 1:
                        if board[i+1][j+1] == check:
                            potential.append([i,j])
                            directions.append('br')

                    #CHECK TOP LEFT
                    if i != 0 and j!= 0:
                        if board[i-1][j-1] == check:
                            potential.append([i,j])
                            directions.append('al')

                    #CHECK BOTTOM LEFT
                    if i != length - 1 and j!= 0:
                        if board[i+1][j-1] == check:
                            potential.append([i,j])
                            directions.append('bl')


        #found = False
        true_spots = []
        correct_direction = []
        for i in range(0,len(directions)):
            found = False
            current_row = potential[i][0]
            current_col = potential[i][1]    
            #Looking Above
            if directions[i] == 'a':
                while current_row > 0 and found == False:
                    current_row = current_row - 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('a')
                        true_spots.append(potential[i])
                        break
            #Looking Below
            elif directions[i] == 'b':
                while current_row < len(board) - 1 and found == False:
                    #print (current_row)
                    current_row = current_row + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('b')
                        true_spots.append(potential[i])
                        break
            #Looking Right
            elif directions[i] == 'r':
                while current_col < len(board) - 1 and found == False:
                    current_col = current_col + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('r')
                        true_spots.append(potential[i])
                        break
            #Looking Left
            elif directions[i] == 'l':
                while current_col > 0 and found == False:
                    current_col = current_col - 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('l')
                        true_spots.append(potential[i])
                        break
            #Looking Top Right Diagonal 
            elif directions[i] == 'ar':
                while current_row - 1 > 0 and current_col + 1 < len(board) - 1 and found == False: 
                    current_row = current_row - 1
                    current_col = current_col + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('ar')
                        true_spots.append(potential[i])
                        break
            #Check top left diagonal  
            elif directions[i] == 'al':
                while current_row - 1 > 0 and current_col - 1 > 0 and found == False: 
                    current_row = current_row - 1
                    current_col = current_col - 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('al')
                        true_spots.append(potential[i])
                        break
            #Check bottom right diagonal 
            elif directions[i] == 'br':
                while current_row + 1 < len(board) - 1 and current_col + 1 < len(board) - 1 and found == False:
                    current_row = current_row - 1
                    current_col = current_col + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('br')
                        true_spots.append(potential[i])
                        break
            #Check bottom left diagonal  
            elif directions[i] == 'bl':
                while current_row + 1 < len(board) - 1 and current_col - 1 > 0 and found == False:
                    current_row = current_row + 1
                    current_col = current_col - 1

                    # print (current_row)
                    # print (current_col)
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('bl')
                        true_spots.append(potential[i])
                        break
            
        return true_spots,correct_direction

    def make_move(self,row,col,neighbors):

        #print (self.player)

        #print (row,col,neighbors)

        board = Othello(self)

        length = len(board.position)

        if self.player == 1:
            check = self.player1
            board.player = 2
        else:
            check = self.player2
            board.player = 1

        #print (self.player)

        #print (len(neighbors))

        found = False
        for i in neighbors:
            #print (i)

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
            #Looking Below
            elif i == 'b':
                while current_row < length - 1 and found == False:
                    board.position[current_row][current_col] = check 
                    current_row = current_row + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
            #Looking Right
            elif i == 'r':
                while current_col < length - 1 and found == False:
                    board.position[current_row][current_col] = check 
                    current_col = current_col + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
            #Looking Left
            elif i == 'l':
                #print ('here')
                #print (check)
                while current_col > 0 and found == False:
                    board.position[current_row][current_col] = check 
                    current_col = current_col - 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
            #Looking Top Right Diagonal 
            elif i == 'ar':
                while current_row > 0 and current_col < length - 1 and found == False: 
                    board.position[current_row][current_col] = check 
                    current_row = current_row - 1
                    current_col = current_col + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
            #Check top left diagonal  
            elif i == 'al':
                while current_row > 0 and current_col > 0 and found == False: 
                    board.position[current_row][current_col] = check 
                    current_row = current_row - 1
                    current_col = current_col - 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
            #Check bottom right diagonal 
            elif i == 'br':
                while current_row < length - 1 and current_col < length - 1 and found == False:
                    board.position[current_row][current_col] = check 
                    current_row = current_row + 1
                    current_col = current_col + 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False
            #Check bottom left diagonal  
            elif i == 'bl':
                while current_row < length - 1 and current_col > 0 and found == False:
                    board.position[current_row][current_col] = check 
                    current_row = current_row + 1
                    current_col = current_col - 1
                    if board.position[current_row][current_col] == check:
                        found = True
                found = False

        #print (self.player)
        return board
    
    def count_positions(self):
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



    def is_Win(self):

        if '.' not in self.position:
            sum1,sum2 = self.count_positions()
            if sum1 != sum2:
                self.is_Terminal = True
            return True
        
        # NO MORE MOVES


        moves1,direction1 = self.find_potential_moves(1)
        moves2,direction2 = self.find_potential_moves(2)

        #print (moves1)

        if moves1 == []:
            # if self.player == 1:
            #     self.player = 2
            # else:
            #     self.player = 

            #print (moves2)
            if moves2 == []:
                sum1,sum2 = self.count_positions()
                if sum1 != sum2:
                    self.is_Terminal = True
                    return True
                
        #SKIPS I need to code this!!
        if moves1 == [] and self.player == 1:
            print ('Here4')
            # return True
            sum1,sum2 = self.count_positions()
            if sum1 != sum2:
                self.is_Terminal = True
                return True
        
        
        if moves2 == [] and self.player2 == 2:
            print ('Here3')
            # return True
            sum1,sum2 = self.count_positions()
            if sum1 != sum2:
                self.is_Terminal = True
                return True

        return False
    
    def is_Tie(self):
        if '.' not in self.position: # and self.is_Win() == False:
            sum1,sum2 = self.count_positions()
            if sum1 == sum2:
                self.is_Terminal = True
                return True
        
        # NO MORE MOVES
        moves1,direction1 = self.find_potential_moves(1)
        moves2,direction2 = self.find_potential_moves(2)

        if moves1 == []:
            # if self.player == 1:
            #     self.player = 2
            # else:
            #     self.player = 1

            
            if moves2 == []:
                sum1,sum2 = self.count_positions()
                if sum1 == sum2:
                    self.is_Terminal = True
                    return True
        
        print (moves1,self.player)
        print (moves2,self.player)

        if moves1 == [] and self.player == 1:
            print ('Here1')
            # return True
            sum1,sum2 = self.count_positions()
            if sum1 == sum2:
                self.is_Terminal = True
                return True
        
        if moves2 == [] and self.player == 2:
            print ('Here2')
            return True
            # sum1,sum2 = self.count_positions()
            # if sum1 == sum2:
            #     self.is_Terminal = True
            #     return True

        return False
    
    def generate_states(self):

        possibles,direction  = self.find_potential_moves(self.player)
        #print (possibles, direction)

        possible,directions = self.unique_values_with_directions(possibles, direction)
        #print (possible, directions)


        actions = []

        #NEED TO CHANGE THIS FOR VALID MOVES ONLY
        for i in range(0,len(possible)):
            actions.append(self.make_move(possible[i][0],possible[i][1],directions[i]))

        # for row in range(0, len(self.position)):
        #     for col in range(0, len(self.position[row])):
        #         if self.position[row][col] == self.empty:
        #             actions.append(self.make_move(row,col))

        #print (actions)

        return actions
    
    def print_board(self):
        board = self.position
        #print ('\t1\t2\t3\t4\t5\t6\t7\t8')
        print ('\t1\t2\t3\t4')
        print("\n".join(str(i + 1) + "\t" +"\t".join(row) for i, row in enumerate(board)))


        ##MOST IMPORTANT FUNCTION!!!
    def isValid(self,row,col):
        board = self.position

        #Can't go outside of board
        if row >= len(board) or col >= len(board) or row < 0 or col < 0:
            return False
        
        #Space is not empty
        elif board[row][col] != '.':
            return False
        
        neighbors = []
        directions = []

        if self.player == 1:
            check = self.player2
            check2 = self.player1
        else:
            check = self.player1
            check2 = self.player2

        #Check above
        if row - 1 >= 0:
            if board[row - 1][col] == check:
                # current_row = row - 1
                # current_col = col 
                # while 
                neighbors.append([row-1,col])
                directions.append('a')
                print ('ABOVE')
        #Check below
        if row + 1 <= len(board)-1:
            if board[row + 1][col] == check:
                neighbors.append([row+1,col])
                directions.append('b')
                print ("BELOW")
        #Check left
        if col - 1 >= 0:
            if board[row][col-1] == check:
                neighbors.append([row,col-1])
                directions.append('l')
                print ("LEFT")
        #Check right
        if col + 1 <= len(board)-1:
            if board[row][col + 1] == check:
                neighbors.append([row,col + 1])
                directions.append('r')
                print ("RIGHT")
        #Check top right diagonal 
        if row - 1 >= 0 and col + 1 <= len(board) - 1:
            if board[row - 1][col + 1] == check:
                neighbors.append([row - 1,col + 1])
                directions.append('ar')
                print ("TOP RIGHT Diagonal")
        #Check top left diagonal  
        if row - 1 >= 0 and col - 1 >= 0:
            if board[row - 1][col - 1] == check:
                neighbors.append([row - 1,col - 1])
                directions.append('al')
                print ("TOP LEFT Diagonal")
        #Check bottom right diagonal 
        if row + 1 <= len(board) - 1 and col + 1 <= len(board) - 1:
            if board[row + 1][col + 1] == check:
                neighbors.append([row + 1,col + 1])
                directions.append('br')
                print ("BOTTOM RIGHT Diagonal")
        #Check bottom left diagonal  
        if row + 1 <= len(board) - 1 and col - 1 >= 0:
            if board[row + 1][col - 1] == check:
                neighbors.append([row + 1,col - 1])
                directions.append('bl')
                print ("BOTTOM LEFT Diagonal")

        #print (neighbors)
        #print (directions)
        if neighbors == []:
            return False,[]

        found = False
        correct_direction = []
        for i in range(0,len(neighbors)):
            current_row = neighbors[i][0]
            current_col = neighbors[i][1]    
            #Looking Above
            if directions[i] == 'a':
                while current_row > 0 and found == False:
                    current_row = current_row - 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('a')
                        #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
            #Looking Below
            elif directions[i] == 'b':
                while current_row < len(board) - 1 and found == False:
                    #print (current_row)
                    current_row = current_row + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('b')
                       #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
            #Looking Right
            elif directions[i] == 'r':
                while current_col < len(board) - 1 and found == False:
                    current_col = current_col + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('r')
                       #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
            #Looking Left
            elif directions[i] == 'l':
                while current_col > 0 and found == False:
                    current_col = current_col - 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('l')
                        #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
            #Looking Top Right Diagonal 
            elif directions[i] == 'ar':
                while current_row - 1 > 0 and current_col + 1 < len(board) - 1 and found == False: 
                    current_row = current_row - 1
                    current_col = current_col + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('ar')
                        #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
            #Check top left diagonal  
            elif directions[i] == 'al':
                while current_row - 1 > 0 and current_col - 1 > 0 and found == False: 
                    current_row = current_row - 1
                    current_col = current_col - 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('al')
                        #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
            #Check bottom right diagonal 
            elif directions[i] == 'br':
                while current_row + 1 < len(board) - 1 and current_col + 1 < len(board) - 1 and found == False:
                    current_row = current_row + 1
                    current_col = current_col + 1
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('br')
                       #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
            #Check bottom left diagonal  
            elif directions[i] == 'bl':
                while current_row + 1 < len(board) - 1 and current_col - 1 > 0 and found == False:
                    current_row = current_row + 1
                    current_col = current_col - 1

                    # print (current_row)
                    # print (current_col)
                    if board[current_row][current_col] == check2:
                        found = True
                        correct_direction.append('bl')
                        #break
                    elif board[current_row][current_col] == '.':
                        break
                found = False
        #print

        if len(correct_direction) == 0:
            found = False
        else:
            found = True

        return found, correct_direction

    def play_game(self):
        tree = MCTS()
        
        self.print_board()

        self.find_potential_moves(self.player)

        while self.is_Terminal == False:
            move = input("Please enter the row and column of your choice of move in the format: row,col ")
            try: 
                row = int(move[0]) - 1
                col = int(move[2]) - 1
            except IndexError:
                move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                row = int(move[0]) - 1 
                col = int(move[2]) - 1

            valid,directions = self.isValid(row,col)
            while valid == False:
                move = input("Invalid move. Please enter the row and column of your choice of move in the format: row,col ")
                try: 
                    row = int(move[0]) - 1 
                    col = int(move[2]) - 1
                except IndexError:
                    pass

                valid,directions = self.isValid(row,col)

            print (directions)
            #a = [[row,col]]
            #a,directions = self.unique_values_with_directions(a,directions)

            print (directions)
            self = self.make_move(row,col,directions)

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
            #print ('HERE')
            #print (self.player)


            #print(self.generate_states())

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