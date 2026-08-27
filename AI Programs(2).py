#(1)Map coloring to csp
colors = ['Red', 'Green', 'Blue']
map = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
color = {}
def valid(region, c):
    for neighbor in map[region]:
        if neighbor in color and color[neighbor] == c:
            return False
    return True
def solve():
    if len(color) == len(map):
        return True
    region = list(map.keys())[len(color)]
    for c in colors:
        if valid(region, c):
            color[region] = c

            if solve():
                return True
            del color[region]
    return False
solve()
print("Map Coloring:")
for region in color:
    print(region, "=", color[region])


#(2)Tic Tac Toe ---------------------------------------------------------------
board = [' ' for i in range(9)]
def display():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
def win(player):
    combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
for turn in range(9):
    display()
    player = 'X' if turn % 2 == 0 else 'O'
    position = int(input(player + " enter position (1-9): ")) - 1
    if board[position] == ' ':
        board[position] = player
    else:
        print("Position already used!")
        continue
    if win(player):
        display()
        print(player, "wins!")
        break
else:
    display()
    print("Draw!")


    
#(3)minimax algorithm for gaming------------------------------------------------
board = [' ' for i in range(9)]
def win(player):
    combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
def minimax(is_max):
    if win('O'):
        return 1
    if win('X'):
        return -1
    if ' ' not in board:
        return 0
    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)
        return best
def best_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
board[0] = 'X'
move = best_move()
board[move] = 'O'
print("Best move for computer:", move + 1)



#(4)alpha beta pruning algorithm for gaming-------------------------------------
def minimax(depth, node, maximizing, values, alpha, beta):
    if depth == 3:
        return values[node]
    if maximizing:
        best = -1000
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
result = minimax(0, 0, True, values, -1000, 1000)
print("Best value:", result)


#(5)Decision tree---------------------------------------------------------------
def decision_tree(age, income):
    if age >= 18:
        if income >= 30000:
            return "Loan Approved"
        else:
            return "Loan Rejected"
    else:
        return "Loan Rejected"

age = int(input("Enter age: "))
income = int(input("Enter income: "))

result = decision_tree(age, income)

print("Decision:", result)



#(6)feed forward neural network-------------------------------------------------
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def neural_network(x1, x2):
    h1 = sigmoid(x1 + x2)
    h2 = sigmoid(x1 - x2)

    output = sigmoid(h1 + h2)

    return output

x1 = float(input("Enter first input: "))
x2 = float(input("Enter second input: "))

result = neural_network(x1, x2)

print("Output:", result)
