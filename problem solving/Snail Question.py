"""

There is a snail on the ground. It wants to climb to the top of a wooden pole with the height of V meters, measuring from the ground level. 
In one day it can climb A meters upwards, however during each night it sleeps, sliding B meters back down. 
Determine the number of days it needs to climb to the top. 

The first and only line of input contains three integers separated by a single space: A, B, and V (1 ≤ B < A ≤ V ≤ 1 000 000 000)

The first and only line of output must contain the number of days that the snail needs to reach the top. 

"""

# Firstly, I just used the 'while loop' to solve this problem.

A, B, V = map(int, input().split())
height = 0
days = 1
while True:
    days += 1
    height += A
    if V <= height:
        print(days)
        break
    height -= B
    

# This way works, but this way of using 'while loop' takes very long time when the value of V is very large.
# So I'm going to make the code more efficient.

a, b, v = map(int, input().split())
ls = 0
if (v - b) % (a - b) != 0:
    ls = ((v - b) // (a - b)) + 1
else:
    ls = ((v - b) // (a - b))
print(ls)

# Snails travel about 'a-b' a day.
# However, when the snail reaches the top point, the snail then does not slip, so it means that the snail climbs up by (v-b).
# If you divide 'a-b' into 'v-b', and the rest is not zero, you need one more day, so add one to the quotient.
# If the rest is 0, print the quotient.
