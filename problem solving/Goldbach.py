"""

A natural number is called a prime number (or a prime) if it is bigger than 1 and has no divisors other than 1 and itself. 
For example, 5 is prime, since no number except 1 and 5 divides it. On the other hand, 6 is not a prime since 6 = 2 × 3 . 
Goldbach's conjecture is one of the famous unsolved problems in number theory and in all of mathematics. 
It states: Every even integer greater than 2 can be expressed as the sum of two primes. Such a number is called a Goldbach number. 
Expressing a given even number as a sum of two primes is called a Goldbach partition of the number. 
For example, 4 = 2 + 2 , 6 = 3 + 3 , 8 = 3 + 5 , 10 = 7 + 3 or 10 = 5 + 5 , 12 = 5 + 7 , 14 = 3 + 11 or 14 = 7 + 7 . 
Note that Goldbach partition has been found for any even interger n less than 10000.
Given any even integer n greater than 2, write a program that prints the two primes of the Goldbach partition of n . 
If there are more than one Goldbach partitions of n, find a partition such that the difference of the two primes of it is minimized. 

"""

def Goldbach():
    check = [False, False] + [True] * 10000
    # find the prime numbers  
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())
        # Half A and B and add and substract 1 to A and B to find out two prime numbers that the difference of the two primes of it is minimised.
        A = n // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()
