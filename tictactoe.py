"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x =0 
    count_o = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O :
                count_o += 1
    if count_x > count_o:
        return O 
    else :
        return X


def actions(board):
    possible = set()
    for i in range(3) :
        for j in range(3):
            if board[i][j] == EMPTY:
                possible.add((i,j))
    return possible 

def result(board, action):
    if action not in actions(board):
        raise Exception("NOT VALID ACTION") 
    
    Result = copy.deepcopy(board)
    Result[action[0]][action[1]] = player(board)
    return Result 


def row_checker (board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True 
    return False 

def col_checker (board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True 
    return False 

def diag_check(board, player):
    count = 0 
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True 
    else:
        return False 

def inv_diag(board, player):
    count = 0 
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True 
    else:
        return False 



def winner(board):
    if row_checker(board,X) or col_checker(board,X) or diag_check(board,X) or inv_diag(board,X):
        return X 
    elif row_checker(board,O) or col_checker(board,O) or diag_check(board,O) or inv_diag(board,O):
        return O
    else:
        return None
    



def terminal(board):
    final = winner(board)
    if (final == X or final == O ):
        return True 
    elif final == None :
        count = 0 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == EMPTY:
                    count += 1 
        if count == 0 :
            return True 
        else :
            return False 
 


def utility(board):
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O :
            return -1
        else:
            return 0


def minimax(board):
    if terminal(board) == True:
        return None 
    
    if player(board) == X :
        outcome = [] 
        for action in actions(board):
            q = (Min_O(result(board,action)), action)
            outcome.append(q)
        l = sorted(outcome, key=lambda x: x[0], reverse=True)
        return l[0][1]
    else :
        outcome = [] 
        for action in actions(board):
            q = (Max_X(result(board,action)), action)
            outcome.append(q)
        l = sorted(outcome, key=lambda x: x[0], reverse= False)
        return l[0][1]



#both the Max_X and Min_O returns utility value 


def Max_X(board):
    v = -math.inf
    
    if terminal(board) == True:
        return utility(board)
    
    for action in actions(board):
        v = max(v,Min_O(result(board, action)))
    return v 

def Min_O(board):
    v = math.inf
    
    if terminal(board) == True:
        return utility(board)
    
    for action in actions(board):
        v = min(v, Max_X(result(board, action)))
    return v