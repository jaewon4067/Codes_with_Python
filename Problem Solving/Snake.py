"""

One of the most popular DOS games is 'Dummy'. The snake is crawling through the board and eating apples that increase its length. 
The game ends when the snake bumps into itself or into the wall. 
Game board consists of NxN squares arranged in N rows and N columns, and some squares contain apples. 
Around the board there is a wall. At the beginning of the game, the snake is located in the top-left corner, its length is equal to 1 and its head is directed towards right. 
Snake is crawling by changing its position during each second according to the following rules: 
first, snake extends its length by spreading to the next square in front of the head (i.e. in the direction of the head),
if there is an apple on that square, tail of the snake does not move (hence, its length is increased by 1 in this step),
if there is no apple, last square of the tail is erased (hence, its length stays unchanged) 
Positions of the apples and movements of the snake are given. Write a program that will calculate the number of seconds until the game ends.

"""

"""

First line of input contains an integer N, 2 ≤ N ≤ 100. 
Following line contains an integer K, 0 ≤ K ≤ 100, the number of apples on the board. 
Following K lines contain coordinates of apples on the board. First number denotes the row and second number denotes the column of the board where the apple is situated. 
There will be no apple at the top-left corner of the board. 
Following line contains an integer number L, 1 ≤ L ≤ 100, the number of times the snake makes a turn. 
Each of the following L lines contains the description of one turn. 
A single turn is described by a number X (positive integer less than or equal to 10,000) and a character C. 
This means that the snake rotates its head 90 degrees left (if C is 'L') or right (if C is 'D') at the end of the Xth second

"""

n = int(input())
k = int(input())

# map
board = [[0] * (n+1) for i in range(n+1)]

# apple info
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

# oper
oper = [input().split() for _ in range(int(input()))]
snake = [(1, 1)] # snake body
# the ending cases
# 1. the snake goes out of the map
# 2. the snake touches its body

d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # East South W N
d_f = 0
score = 0 # time
x, y = 1, 1

while True:
    score += 1
    # next -> x, y
    x += d[d_f][0]
    y += d[d_f][1]
    if 1 <= x <= n and 1 <= y <= n:
        snake.append((x, y)) # expand the length
        for i in snake[:-1]: # hit its body
            if (x, y) == i:
                print(score)
                exit(0)
        if board[x][y] == 0: # remove tail
            snake.pop(0)
        if board[x][y] == 1:
            board[x][y] = 0
    else:
        print(score)
        break
    if oper and score == int(oper[0][0]):
        if oper[0][1] =='D': # right 90 degrees
            d_f = d_f + 1 if d_f < 3 else 0
            oper.pop(0)
        elif oper[0][1] == 'L': # left 90 degrees
            d_f = d_f - 1 if d_f > 0 else 3
            oper.pop(0)

