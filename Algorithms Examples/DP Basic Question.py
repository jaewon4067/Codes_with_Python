"""

I want to write a function 'power' that calculates square. The funcion 'power' receives natural number x and natural number y as parameters, and returns x^y.
The easiest way to think of solving this is to simply multiply x by y times with a loop.

"""

def power(x, y):
    total = 1
    
    # Multiple x, y times
    for i in range(y):
        total *= x
    return total

"""

The time complexity of this algorithm is O(y). 
I want to make it more efficient with the time complexity of O(lgy).

"""

# To look at this question from a different prespective, I'm going to write a recursive function instead of using loops.
# To solve this question for O(lgy), recursive form should be a form as power (x, y // 2) instead of power (x, y - 1).

def power(x, y):
    if y == 0:
        return 1

    # To only calculate once, save it in subresult.
    subresult = power(x, y // 2)
    
    # Divide the question to the same questions (cases of even and odd number)
    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult


# Test
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))

"""

How many function calls are there to calculate 2^8?
power(2, 8)
power(2, 4)
power(2, 2)
power(2, 1)

Called 4 times when y is 8. There's a total of lgy+1 calls.
Therefore, the time complexity of this algorithm is O(lgy).

"""














