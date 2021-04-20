"""
Cho Kyu-hyun and Baek Seung-hwan are employees of Turret. But it doesn't have much presence, so it doesn't take up the population. 

Lee Seok-won ordered Cho Kyu-hyun and Baek Seung-hwan to calculate the position of the opponent Marine (Ryu Jae-myung). 
Cho Kyu-hyun and Baek Seung-hwan calculated the distance from their turret position to the current enemy, respectively.

Given the coordinates of Cho Kyu-hyun (x1, y1) and Baek Seung-hwan (x2, y2), 
and the distance r1 from Ryu Jae-myung calculated by Cho Kyu-hyun and r2 from Ryu Jae-myung calculated by Baek Seung-hwan, write a program that outputs the number of possible coordinates.
"""

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    R = [r1, r2, r]
    m=max(R);
    R.remove(m)

    if r==0 and r1==r2:
        print(-1)
    else:
        if r == r1+r2 or m == sum(R):
            print(1)
        else:
            if m > sum(R):
                print(0)
            else:
                print(2)
