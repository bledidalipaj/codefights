"""
Description
***********

Given P, find the smallest number N such that N! has exactly P trailing zeros.

Example

Factorial(2) = 10;
Factorial(10) = 45;
Factorial(1) = 5.
Input/Output

[time limit] 4000ms (py)
[input] integer P

Constraints:
1 ≤ P ≤ 2 * 108.

[output] integer

The smallest number N such that N! has P trailing zeros, or -1 if there is no such number.

# https://codefights.com/challenge/FAtkuto4nPpD9JPQk/main #
"""
def Factorial(P):
    trailing_zeros = lambda n: n and n / 5 + trailing_zeros(n / 5)
    
    left_bound = 0
    right_bound = 2 * 10 ** 10
    ans = -1
    
    while True:
        v = (left_bound + right_bound) / 2
        zeros = trailing_zeros(v)
        if P < zeros:
            right_bound = v - 1 
        if P > zeros:
            left_bound = v + 1
        if P == zeros:
            if ans == v:
                break
            right_bound = v - 1 
            ans = v
        if left_bound > right_bound:
            break
    return ans 