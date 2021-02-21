"""

Bulls and cows

-The computer randomly selects three different numbers between 0 and 9. (Ex, a computer can pick 593 or 184)
-You then guess the exact number that computer picked.
-When you enter a number you guessed, the computer tells you the number of bulls and cows.
-If your try has matching digits on the exact places, they are bulls.
-If you have digits from the number from the computer, but not on the right places, they are cows.
-You have unlimited opportunities. It is recorded how many attempts you have made.
-The game ends when 3 bulls.

"""

from random import randint

#computer generates numbers
def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers

def take_guess():
    new_guess = []
    while len(new_guess) < 3:
        num = int(input("Enter {}th number: ".format(len(new_guess) + 1)))

        if num < 0 or num > 9:
            print("Enter the number between 0 to 9.")
        elif num in new_guess:
            print("You have already entered this number. Please re-enter the number.")
        else:
            new_guess.append(num)

    return new_guess

def get_score(guess, answer_list):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == answer_list[i]:
            strike_count += 1
        elif guess[i] in answer_list:
            ball_count += 1

    return strike_count, ball_count

# The game starts from here.
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("You got it. You have tried {}th times.".format(tries))
