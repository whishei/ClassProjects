import numpy as np
import math
import random

#Defining a node (current state of the board)
class Node:

    def __init__(self,board,parent):
        #Initializing a node, setting the parent, the score, the number of times visited, etc. 
        
        self.board = board

        if self.board.is_win() or self.board.is_tie():
            self.leaf = True
        else:
            self.leaf = False

        self.expanded = self.leaf
        self.parent = parent
        self.n = 0
        self.w = 0
        self.children = {}

#Defining the MCTS class
class MCTS:
    
    def search(self, inital):
        #Searching for the best move to make at the current state (initial)

        self.root = Node(inital, None)
        for it in range(0, 2000):
            current = self.descend(self.root)
            score = self.simulate(current.board)
            self.back_prop(current,score)

        try:
            return self.best_move(self.root,0)
        except: 
            pass

    
    def descend(self,node):  
        # Selecting which nodes to descend down, if not at a leaf, need to go down more. 

        while node.leaf == False:
            if node.expanded == True:
                node = self.best_move(node,2)
            else:
                return self.expand(node)
        return node

    
    def expand(self, node):
        # Creating a new node for the state if it has not been reached yet. 

        states = node.board.generate_states()

        for state in states:
            if str(state.position) not in node.children:
                new_node = Node(state,node)
                node.children[str(state.position)] = new_node
                if len(states) == len(node.children):
                    node.expanded = True
                return new_node
 

    def simulate(self, board):
        # Simulating out the rest of the play if the game is not over yet. 

        while board.is_win() == False: 
            try:
                board = random.choice(board.generate_states()) 
            except:
                return 0
            
        #MCTS is set up to always be looking at the game as if they are the first player, even though the computer is second. 
        if board.player == 1: 
            return -1
        else:
            return 1
    
    def back_prop(self,current,score):
        #Back propagating the score and the number of visits to all nodes traveled for the best selected move

        while current is not None:
            current.n = current.n + 1
            current.w = current.w + score
            current = current.parent

    def best_move(self,node,c):
        # Selecting the best move (Maximizing UCB for player to win, minimizing UCB for opponent) 

        best_score = float('-inf')
        best_moves = []


        for child in node.children.values():
            if child.board.player == 1:
                current_player = -1
            else:
                current_player = 1

            UCB = current_player*child.w/child.n + c*math.sqrt(math.log(node.n)/child.n)

            if UCB > best_score:
                best_score = UCB
                best_moves = [child]

            elif UCB == best_score:
                best_moves.append(child)

        return random.choice(best_moves)

