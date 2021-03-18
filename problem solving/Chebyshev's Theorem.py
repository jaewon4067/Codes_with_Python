"""

If n is a positive integer, there exists at least one prime number greater than n and less than or equal to 2n. 
This fact is known as Chebyshev's theorem or the Bertrand-Chebyshev theorem, which had been conjectured by Joseph Louis François Bertrand (1822–1900) and was proven by Pafnuty Lvovich Chebyshev (Пафнутий Львович Чебышёв, 1821–1894) in 1850. 
Srinivasa Aiyangar Ramanujan (1887–1920) gave an elementary proof in his paper published in 1919. Paul Erdős (1913–1996) discovered another elementary proof in 1932.
For example, there exist 4 prime numbers greater than 10 and less than or equal to 20, i.e. 11, 13, 17 and 19. 
There exist 3 prime numbers greater than 14 and less than or equal to 28, i.e. 17, 19 and 23.
Your mission is to write a program that counts the prime numbers greater than n and less than or equal to 2n for each given positive integer n. 
Using such a program, you can verify Chebyshev's theorem for individual positive integers.

"""

from math import sqrt

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0

    for i in range(n+1, 2*n+1):
        if i == 1:
            continue
        elif i ==2:
            cnt += 1
            continue
        else:
            for j in range(2, int(sqrt(i)+1)): # for me, this part was littel bit hard to think of.
                if i % j ==0:
                    break
                else:
                    cnt += 1
    print(cnt)
