"""

in one word, find out which alphabet is used the most (assume all alphabets are captial)


"""


word = input()

word = word.upper()

alphabet = {}

for i in word:
    if i in alphabet: alphabet[i] += 1
    else: alphabet[i] = 1

answer = 0
big = 0

for i in alphabet:
    if alphabet[i] > big:
        big = alphabet[i]
        answer = i
    elif alphabet[i] == big:
        answer = '?'

print(answer)

