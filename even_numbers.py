"""
Description
***********
Number X is called twice even if it is divisible by 2, and number X / 2 is also divisible by 2, yet X / 2 / 2 is not. For example, X = 12 
is twice even, since 12 / 2 = 6 - even, and 6 / 2 = 3 is not even.

You're given two numbers: N and P. Find the largest number X, such that 1 ≤ X ≤ P and X is divisible by 2 exactly N times. If there's no 
such number, return -1 instead.

Example

For N = 2 and P = 15, the output should be
EvenNumbers(N, P) = 12.

12 / 2 = 6 and 6 / 2 = 3, which is not even.

Input/Output

[time limit] 4000ms (py)
[input] integer N

Constraints:
0 ≤ N ≤ 30.

[input] integer P

Constraints:
1 ≤ P ≤ 2 · 109.

[output] integer

The largest number X, such that 1 ≤ X ≤ P and X is divisible by 2 exactly N times. If this number does not exist return -1 instead.

# Challenge's link: http://codefights.com/challenge/4HANW3Rbjcs9TZmMM/main #
"""

def EvenNumbers(N, P):
	# the numbers wich can be divided exactly N times by 2
    # have the following form 2 ** N * c, where c is an odd number
    # for example when N = 2 
    # the numbers wich are divisible by 2 exactly two times are the following
    # 2 ** 2 * 1 = 4
    # 2 ** 2 * 3 = 12
    # 2 ** 2 * 5 = 20
    # 2 ** 2 * .. = ..
    n = 2 ** N 
    c = P / n
    
    # check if c is odd, if not reduce it by 1
    if c % 2 == 0:
        c -= 1
    
    return n * c if c != -1 else -1