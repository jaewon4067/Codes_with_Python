"""

Do you know the top game in Hanoi? The goal of this game is to move all the disks on the left column to the right column. 
There are two rules to follow.:
1. Only one disk can be moved at a time.
2. A large disk should not be on a small disk.

"""

# There are recursive and base cases.
# Recursive case: The current problem is too large, and you are recursively solving smaller problems of the same form.
# Base case: the problem is already small enough, so you can get the answer right away without breaking it down into smaller parts.
# Let's think about what base case is first.


def move_disk(disk_num, start_peg, end_peg):
    print("Move the plate %d from the column %d to the column %d" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # base case: End the function if there is no disks left.
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg # start_peg + other_peg + end_peg = 6
        
        # 1. Exclude the biggest disk, move the rest disks from start_peg to other_peg.
        hanoi(num_disks - 1, start_peg, other_peg)
        
        # 2. Move the biggest diks from start_peg to end_peg.
        move_disk(num_disks, start_peg, end_peg)
        
        # 3. Move the rest disks from other_peg to end_peg.
        hanoi(num_disks - 1, other_peg, end_peg)

# Test
hanoi(3, 1, 3)

# When I first tried this question, I was so confused, but I tried it step by step and I could solve it!
