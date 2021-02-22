"""

I want to use the Binary Search algorithm to determine if a number is included in the list (binary search algorithms assume ordered lists).
This algorithm cannot be applied unless it is an ordered list.

"""

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    # Repeat the while loop until start_index is equal or greater than end_index.
    # And if the while loop ends, the number we are looking for is not in the list.
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

"""

That's how we implemented binary Search.
Binary search reduces the range of the search by half (approximately) every time, which is very efficient.

So, I'm going to try to solve the problem recursively this time.

"""

def binary_search(element, some_list, start_index=0, end_index=None):
    # If 'end_index' is not given, set the last element as a 'end_index.
    if end_index == None:
        end_index = len(some_list) - 1

    # If start_index is greater than end_index, the number is not in the some_list.
    if start_index > end_index:
        return None
      
    # Find the middle index.
    mid = (start_index + end_index) // 2
  
    # Check if this index is the number we are looking for.
    if some_list[mid] == element:
        return mid

    # If the number is smaller than the middle index, search left hand side of the list.
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # If the number is greater than the middle index, search right hand side of the list.
    else:
        return binary_search(element, some_list, mid + 1, end_index)        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

# The time complexity is 'lg(n)', because the range of the search is reduced by half.
