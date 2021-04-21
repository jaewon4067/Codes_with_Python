"""
Bessie loves board games and role-playing games so she persuaded Farmer John to drive her to the hobby shop where she purchased three dice for rolling. 
These fair dice have S1, S2, and S3 sides respectively (2 <= S1 <= 20; 2 <= S2 <= 20; 2 <= S3 <= 40).

Bessie rolls and rolls and rolls trying to figure out which three-dice sum appears most often.

Given the number of sides on each of the three dice, determine which three-dice sum appears most frequently. 
If more than one sum can appear most frequently, report the smallest such sum.
"""

s1, s2, s3 = map(int, input().split())
li = [0]*81
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            li[i+j+k] += 1
print(li.index(max(li)))
