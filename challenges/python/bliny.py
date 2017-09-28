"""
Mom bakes the bliny (flat pancakes) and puts them on a plate one on top of another: the first one, then the second and so on. From time 
to time one of her numerous kids rushes into the kitchen, grabs the topmost pancake, eats it and runs away.

Determine if the bliny could have been eaten in the given order, where order is some rearrangement of the numbers from 1 to n.

Example

For order = [2, 1, 3], the output should be
bliny(order) = true.

First kid's intrusion happened when the pancake 2 was ready. Then the second child ate the pancake 1. Then the mother baked pancake 3 and 
it was eaten.

For order = [3, 1, 2], the answer should be
bliny(order) = false.

Input/Output

[time limit] 4000ms (py)
[input] array.integer order

Array of rearranged integers 1 to n.

Constraints:
1 ≤ order.length ≤ 20.

# Challenges' link: https://codefights.com/challenge/BK3F7WE3LAKMX5oG4/main #
"""

def bliny(order):
    used = []
    stack = []
    
    for i in order:
        for j in range(1, i + 1):
            if j not in used and j not in stack:
                stack.append(j)
        used.append(i)
        if stack.pop() != i:
            return False
    return True