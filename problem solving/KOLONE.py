"""

When moving, ants form rows so that each ant except the first is behind another ant. 
It is not widely known what happens when two rows of ants moving in opposite directions run into each other in a passage too narrow for both rows to pass through. 
One theory says that, in that situation, ants will jump over each other. 
From the moment the rows meet, each second every ant jumps over (or gets jumped over, as they agree upon) the ant in front of himself so that the two ants swap places, 
but only if the other ant is moving in the opposite direction. Find the order of the ants after T seconds.

"""

"""

The first line contains two integers N1 and N2, the numbers of ants in the first and second rows, respectively.
The next two rows contain the orders of ants in the first and second row (first to last). 
Each ant is uniquely determined by an uppercase letter of the English alphabet (this letter is unique between both rows). 
The last line of input contains the integer T (0 ≤ T ≤ 50). 

"""

import sys

N1, N2 = map(int, sys.stdin.readline().split(" "))
ants1 = list(sys.stdin.readline().rstrip())
ants2 = list(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline())

dir = {} # save the direction
for ant in ants1:
    dir[ant] = 0
for ant in ants2:
    dir[ant] = 1

ants1.reverse()
ants1.extend(ants2) # made in order

for _ in range(T):
    i = 0
    while i < len(ants1) - 1:
        if dir[ants1[i]] == 0 and dir[ants1[i+1]] == 1:
            ants1[i], ants1[i+1] = ants1[i+1], ants1[i]
            i += 1
        i += 1

for ant in ants1:
    print(ant, end = '')
    


# I always prefer using list but it was a good practice using dir instead of list. 
