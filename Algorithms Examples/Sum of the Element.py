"""

I would like to check if there is a combination of two elements in [1, 2, 5, 6, 7, 9, 11] that sum to 15. 
The sum of the two elements 6 and 9 is 15. I want to make a function to tell me if there's a combination.
The function sum_in_list receives an integer list sorted by the integer search_sum. 
It returns to Boolean whether there is a combination of the two elements in the sort_list that is search_sum or not.
For example, sum_in_list (15, [1, 2, 5, 6, 7, 9, 11]) returns the called True.

"""

# With the Brute Force approach, I can easily check all possible cases to get the answer.

def sum_in_list(search_sum, sorted_list):
    for i in range(len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if sorted_list[i] + sorted_list[j] == search_sum:
                return True
    return False

"""

The time complexity is O(n^2), which is not efficient. 
I found out that it is possible to solve the question by using the fact that the input list is sorted.
I thought about using binary search to create functions more efficiently than O(n^2).
It takes O(lgn), therefore, all together, in this case, it would take O(nlgn). 
(I won't code this part)
I'm going to try to solve this question with O(n) of the time complexity.

"""

def sum_in_list(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    
    while low < high:
        candidate_sum = sorted_list[low] + sorted_list[high]
        
        if candidate_sum == search_sum: # If the sum is the number we are looking for.
            return True
        
        if candidate_sum < search_sum:  # If the sum is smaller than the number we are looking for.
            low += 1
        
        else: # If the sum is greater than the number we are looking for.
            high -= 1
    
    # Cannot find any combinations, so return 'False'
    return False
    
# Test
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))








