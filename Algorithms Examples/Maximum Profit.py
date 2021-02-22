"""

I'm going to create a function called 'sublist_max', which finds the interval in which the share has the largest return during a certain period of time.

First of all, the function sublist_max receives a list of the profits as a parameter. The list includes several days of profit. 
For example, if the list is [7, -3, 4, -8,],
I earn seven dollars on the first day, lose three dollars on the second day, earn four dollars on the third day, and lose eight dollars on the last day.
The sublist_max function returns the max profit from the interval, in this case, it's 7-3+4=8.

I'm going to solve this problem using the Brute Force method first.

"""

def sublist_max(profits):
    max_profit = profits[0] # max profit
    
    for i in range(len(profits)):
        # Save the sum of the profit from index i to index j.
        total = 0
        
        for j in range(i, len(profits)):
            # Calculate the sum of the profit from index i to index j.
            total += profits[j]
            
            # If the sum of the profit from i index to j index is maximum, update max_profit.
            max_profit = max(max_profit, total)

    return max_profit


# Test
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))

"""

Let's say that the length of the input list 'profit' is 'n'. 
There are two repetitive loops, therefore, the time complexity is O(n^2).

This time, I'm going to solve the same question by using Divide and Conquer. Time complexity should be O(nlgn).
This 'sublist_max' function receives three parameters in this question.
-profits: a list of profit for several days
-start: the start index of the interval to look at
-end: the end index of the interval to look at

"""

"""

Divide and Conquer will be divided into three stages.

Divide: Divide a given problem into the same form of partial problems.
Conquer: Solve each part of the problem.
Combine: Using the answers of partial problems, find the final answer.

In this question, they will be:
Divide: Divide the interval into left and right halves.
Conquer: Calculate the maximum possible profit from the left half and the maximum possible profit from the right half respectively.
Combine: Choose the largest of them by comparing the maximum possible profit in the left half and the right half, and the maximum possible profit crossing the centre.

"""
def max_crossing_sum(profits, start, end): # This was hard for me to understand this concept.
    mid = (start + end) // 2      # Middle index

    '''
    Calculate the max profit from left hand side.
    Look for the max profit from index mid to index 0.
    '''
    left_sum = 0                  # accumulated profit (left hand side)
    left_max = profits[mid]       # max profit (left hand side); reset profit to index mid.

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    '''
    Calculate the max profit from right hand side.
    Look for the max profit from index mid+1 to index end.
    '''
    right_sum = 0                 # accumulated profit (right hand side)
    right_max = profits[mid + 1]  # max profit (right hand side); reset profit to index mid+1.

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max(profits, start, end):
    # If there is one element, return it.
    if start == end:
        return profits[start]

    # Mid index
    mid = (start + end) // 2

    # Find the max profit in each case.
    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    # Return the biggest one of the above three.
    return max(max_left, max_right, max_cross)


# 
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))

"""

Let's say the length of the list 'profit' is n.
First of all,the time complexity of max_crossing_sum is O(n) because there are two For Loops.
Since we can reduce the range of the list by about half, time complexity here is lgn.
Therefore, the total time complexity is O(nlgn).

Can we educe time complexity to even O(n)?

"""

def sublist_max(profits):
    max_profit_so_far = profits[0] # the answer of partial questions from loop to the present
    max_check = profits[0] # the maximum sum of intervals including the endmost element 
    
    # Save maximum profit up until each element from for loop.
    for i in range(1, len(profits)):
        # Choose the max profit with the interval including the new element.
        max_check = max(max_check + profits[i], profits[i])
        
        # Find the maximum profit 
        max_profit_so_far = max(max_profit_so_far, max_check)
    
    return max_profit_so_far
    
"""

The length of list 'profit' is n, so the total time complexity is O(n).
It's much more efficient in terms of time complexity than using the Brute Force method and using the Divide and Conquer method.

"""
