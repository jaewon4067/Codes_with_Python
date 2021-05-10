"""

Lumberjack Mirko needs to chop down M metres of wood. It is an easy job for him since he has a nifty new woodcutting machine that can take down forests like wildfire. 
However, Mirko is only allowed to cut a single row of trees.
Mirko's machine works as follows: Mirko sets a height parameter H (in metres), 
and the machine raises a giant sawblade to that height and cuts off all tree parts higher than H (of course, trees not higher than H meters remain intact).
Mirko then takes the parts that were cut off. 
For example, if the tree row contains trees with heights of 20, 15, 10, and 17 metres, and Mirko raises his sawblade to 15 metres, 
the remaining tree heights after cutting will be 15, 15, 10, and 15 metres, respectively, 
while Mirko will take 5 metres off the first tree and 2 metres off the fourth tree (7 metres of wood in total).
Mirko is ecologically minded, so he doesn't want to cut off more wood than necessary. 
That's why he wants to set his sawblade as high as possible. Help Mirko find the maximum integer height of the sawblade that still allows him to cut off at least M metres of wood.

"""

N,M = list(map(int, input().split(' ')))
heights = list(map(int, input().split(' ')))
amount = 0
cut_height = max(heights)
while amount < M:
    cut_height -= 1
    amount = 0
    for height in heights:
        if cut_height < height:
            amount += (height - cut_height)
    print(amount)
    print(cut_height)

    
"""
By using binarysearch
"""

N, M = map(int, input().split())
heights = list(map(int, input().split()))

min_height, max_height = 1, max(heights)
H = 0

while (min_height <= max_height):
    mean_height = (min_height + max_height) // 2

    cut_num = 0
    for height in heights:
        if (height > mean_height):
            cut_num += (height - mean_height)

    # if the length was enough, 
    # do one more if statement to check if we can save more trees.
    if (cut_num >= M):
        H = mean_height
        min_height = mean_height + 1

    # If the length isn't enough,
    # reduce maximum length by 1.
    elif (cut_num < M):
        max_height = mean_height - 1

print(H)    
