"""

In “Blackjack”, a popular card game, the goal is to have cards which sum up to largest number not exceeding 21. Mirko came up with his own version of this game.

In Mirko‟s game, cards have positive integers written on them. The player is given a set of cards and an integer M. He must choose three cards from this set so that their sum comes as close as possible to M without exceeding it. This is not always easy since there can be a hundred of cards in the given set.

Help Mirko by writing a program that finds the best possible outcome of given game.

"""

n,m = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))

result = 0
length = len(cards)

for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = cards[i]+cards[j]+cards[k]
            if sum <= m:
                result = max(sum, result)

print(result)
