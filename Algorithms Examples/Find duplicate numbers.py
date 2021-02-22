"""

In the list, which is the size of (N +1), any natural number from 1 to N is assigned as an element. Then some numbers will be repeated at least once.
I want to find a recurring element in this list.
I can find any 'one number' that overlaps. 
Design a time-efficient function to find overlapping numbers.

"""

def find_same_number(some_list):
    # Check all the possible combinations, and return the element.
    for i in range(len(some_list)):
        for j in range(i + 1, len(some_list)):
            if some_list[i] == some_list[j]:
                return some_list[i]

print(find_same_number([1, 1, 1, 6, 2, 2, 3]))

"""

Im this case, the time complexity is O(n^2). This is an easy way to solve this question, but not quite efficient.
Let's think of an efficient way rather than checking all the combinations.

"""

# There are two ways to store multiple elements, list and dictionary. It doesn't matter which one we use, but I'll use the dictionary in this case. 
# I'm going to add the elements that are not in the dictionary and return if the element is already appended in the dictionary.

def find_same_number(some_list):
    # A dictionary to store elements
    elements_seen_so_far = {}

    for element in some_list:
        # If the element is already in the dictionary, return the element.
        if element in elements_seen_so_far:
            return element

        # Store the element in the dictionary.
        elements_seen_so_far[element] = True

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

"""

If the length of input list is n, the complexity of this algorithm is O(n).

I want to make this question a bit barder by adding two restrictions.
Firstly, I want to use space complexity less than O(n), which means I cannot use dictionaries or lists.
I also don't want to replace or modify elements in the list called 'some_list'.
I'm going to solve the same question I did above with two restrictions.

"""

def find_same_number(some_list, start = 1, end = None):
    if end == None:
        end = len(some_list) - 1

    # Return when it finds the repeated element.
    if start == end:
        return start

    # Find the mid 
    mid = (start + end) // 2

    # Count the number in left range. Don't have to count rigth range cos I can subtract from left.
    left_count = 0

    for element in some_list:
        if start <= element and element <= mid:
            left_count += 1

    # Either left or right range, choose the range where there are more than half of the numbers.
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)

    return find_same_number(some_list, mid + 1, end)

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

"""

When we say the length of the input list is n, each time you go around the list, the time complexity is O(n).
The size of the range starts at (n-1)/2, and continues to be halved. In the worst case scenario, it takes O(lg(n)) to reach one natural number.
The final time complexity is O(nlgn).

"""
