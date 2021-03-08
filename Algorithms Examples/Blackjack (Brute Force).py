"""

In “Blackjack”, a popular card game, the goal is to have cards which sum up to largest number not exceeding 21. Mirko came up with his own version of this game.
In Mirko‟s game, cards have positive integers written on them. 
The player is given a set of cards and an integer M. He must choose three cards from this set so that their sum comes as close as possible to M without exceeding it. 
This is not always easy since there can be a hundred of cards in the given set.
Help Mirko by writing a program that finds the best possible outcome of given game.

The first line of input contains an integer N (3 ≤ N ≤ 100), the number of cards, and M (10 ≤ M ≤ 300 000), the number that we must not exceed.
The following line contains numbers written on Mirko‟s cards: N distinct space-separated positive integers less than 100 000.
There will always exist some three cards whose sum is not greater than M.

"""

n, m = list(map(int, input().split(' ')))
card_list = list(map(int, input().split(' ')))

result = 0
length = len(card_list)

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = card_list[i]+card_list[j]+card_list[k]
            if sum <= m:
                result = max(result, sum)

print(result)
