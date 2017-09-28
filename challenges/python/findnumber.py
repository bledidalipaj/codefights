"""
This is a reverse challenge, have fun!

Input/Ouput

[time limit] 4000ms (py)
[input] integer n

Constraints:
0 ≤ n ≤ 100.

[output] integer

Input:
n: 1
Expected Output:
123

Input:
n: 2
Expected Output:
456

Input:
n: 3
Expected Output:
789

# Challenge's link: https://codefights.com/challenge/o6Jz5K69quZeuAckn #
"""
def findNumber(n):
    a = 1 + 3 * (n - 1) if n > 0 else 0
    b = 2 + 3 * (n - 1) if n > 0 else 0
    c = 3 + 3 * (n - 1) 
    
    return int("".join(map(str, [a, b, c])))

def findNumber(n):
    res = []
    
    for i in range(1, 4):
        value = i + 3 * (n - 1) if n > 0 else 0
        res.append(value)
    return int("".join(map(str, res)))