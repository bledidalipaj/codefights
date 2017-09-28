"""
Consider a sequence in which each element is obtained from the previous one by applying some function f to it.
Given three consecutive elements from this sequence as an array seq, your task is to find and return the function 
f used to build it.

It is guaranteed that the given function is not a constant and it not an identity function.

Example

For seq = [7,8,9], the output should be
findTheFormula(seq) ="n+1".

Let f = n + 1. In this case f(7) = 8, and f(8) = 9, which coincides with the given elements. Thus, the answer is 
"n+1".

Input/Output

[time limit] 4000ms (py3)
[input] array.integer seq

Constraints:
seq.length = 3,
-106 ≤ seq[i] ≤ 106.

[output] string

Function f in the format kn[+-]b. If b is equal to zero, it should be omitted. If the absolute value of k is 1, it should 
be omitted as well.

# Challenge's link: https://codefights.com/challenge/PR8br4c5qagRqmoab #
"""
def findTheFormula(seq):
    # y = ax + b
    a = (seq[2] - seq[1]) // (seq[1] - seq[0])
    b = seq[1] - a * seq[0]
    
    if abs(a) == 1:
        a = '' if a > 0 else '-'
    else:
        a = str(a)
    
    if b == 0:
        b = ''
    else:
        b = '+' + str(b) if b > 0 else str(b)
    return a + 'n' + b