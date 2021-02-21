"""

I'm going to create lottery simulation programme.
The numbers are from 1 to 45. The computer randomly picks six regular numbers and one bonus number. 
You choose six different numbers.
The winning amount is determined by the rules below.
1. All 6 numbers you picked and the six regular numbers match ( 1M dollars).
2. Five numbers you picked and the five regular numbers and one of your numbers matches the bonus numbers (50K dollars).
3. Five numbers you picked and the five regular numbers match (1K dollars).
4. Four numbers you picked and the four regular numbers match (50 dollors).
5. Three numbers you picked and the three regular numbers match (5 dollors).

"""


from random import randint

def generate_numbers(n):
    numbers = [] 

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)
    return numbers

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count

# We have to look at two things to know the price money. 
# 1. How many of the six numbers and six general numbers match?
# 2. How many of the six numbers and one bonus number match?

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
        
# test
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
