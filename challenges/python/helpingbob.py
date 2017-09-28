"""
Bob is standing at the cell (0, 0) of a rectangular grid, and he wants to get to the cell (x, y) in the minimum number 
of moves. Of course there are quite a few possible paths, but Bob can't take some of them: there are hungry dragons 
waiting for him to make a wrong move! Luckily, Bob knows that the kth lexicographically smallest shortest path is safe, 
so is planning to take it.

Bob can get to his destinations making either horizontal (to the right) or vertical (down) moves. Each path can thus be 
represented as a sequence of moves denoted by letters 'H' and 'V'. For example, a possible way to get from (0, 0) to (2, 3) 
is :HVVVH".

Given the value of k find the kth (0-based) lexicographically smallest path from (0, 0) to (x, y) that uses the minimum 
number of moves.

Example

For x = 2, y = 3 and k = 4, the output should be

helpingBob(x, y, k) = "VHHVV".

Here are the first 5 paths:

"HHVVV";
"HVHVV";
"HVVHV";
"HVVVH";
"VHHVV", the answer.
Input/Output

[time limit] 4000ms (py3)
[input] integer x

X (horizontal) coordinate of the destination.

Constraints:

0 ≤ x ≤ 10.

[input] integer y

Y (vertical) coordinate of the destination.

Constraints:

0 ≤ y ≤ 10.

[input] integer k

0-based number of the safe path.

Constraints:

0 ≤ k < number_of_paths.

[output] string

kthlexicographically smallest path.
"""
def helpingBob(x, y, k):
    path = ['H'] * x + ['V'] * y
    for _ in range(k):
        rightmostH = -1
        cntV = 1 if path[-1] == 'V' else 0
        cntH = 1 if path[-1] == 'H' else 0
        for j in range(x + y - 2, -1, -1):
            if path[j] == 'V':
                cntV += 1
            elif path[j + 1] == 'V':
                rightmostH = j
                cntH += 1
                break
            else:
                cntH += 1
        path = path[:rightmostH] + ['V'] + ['H'] * cntH + ['V'] * (cntV - 1)
    return ''.join(path)