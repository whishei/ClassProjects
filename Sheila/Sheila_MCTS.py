import numpy as np
import math
import random

class Node:
    def __init__(self,board,parent):

        self.board = board

        if self.board.is_Win() or self.board.is_Tie():
            self.leaf = True
        else:
            self.leaf = False

        self.expanded = self.leaf

        self.parent = parent

        self.n = 0

        self.w = 0

        self.children = {}

class MCTS:
    #def __init__(self):

        #self.c = 0
        #return NotImplementedError() 
    
    def search(self, inital):

        self.root = Node(inital, None)

        for it in range(0, 1000):
            
            current = self.descend(self.root)

            score = self.simulate(current.board)

            #print (score)

            self.back_prop(current,score)

        #print (self.root.w)
        try:
            #print ('HERE')
            return self.best_move(self.root,0)
            
        except: 
            pass

    
    def descend(self,node):  

        while node.leaf == False:

            if node.expanded == True:

                node = self.best_move(node,2)
            
            else:
                return self.expand(node)
        
            #print (node.leaf)
        return node

    
    def expand(self, node):

        states = node.board.generate_states()

        for state in states:

            if str(state.position) not in node.children:

                new_node = Node(state,node)

                node.children[str(state.position)] = new_node

                if len(states) == len(node.children):
                    node.expanded = True

                return new_node
        #print ('Should not get here')
 

    def simulate(self, board):

        #print (board.print_board())

        while board.is_Win() == False and board.is_Tie() == False: 

            try:

                board = random.choice(board.generate_states()) 
            
            except:

                return 0

            #print (board.print_board())
            
        if board.player == 2:
            return -1
        else:
            return 1

        #return NotImplementedError()
    
    def back_prop(self,current,score):

        while current is not None:
            
            current.n = current.n + 1

            current.w = current.w + score

            current = current.parent

        #return NotImplementedError()

    def best_move(self,node,c):

        best_score = float('-inf')
        best_moves = []

        for child in node.children.values():

            if child.board.player == 2:
                current_player = -1
            else:
                current_player = 1


            UCB = current_player*child.w/child.n + c*math.sqrt(math.log(node.n)/child.n)
            #print (UCB, best_score)

            if UCB > best_score:
                best_score = UCB
                best_moves = [child]

            elif UCB == best_score:
                best_moves.append(child)

        return random.choice(best_moves)

