"""
Given integers a and b, calculate the sum of all the digits that appear in numbers in the range [a, b].

Example

For a = 1 and b = 10, the output should be
DigitSumRange(a, b) = 46.

Here's how the answer is calculated: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46.

Input/Output

[time limit] 4000ms (py)
[input] integer a

Constraints:
0 ≤ a ≤ b.

[input] integer b

Constraints:
a ≤ b ≤ 106.

[output] integer

Sum of digits of all the numbers in range [a, b].

# Challenge's link: https://codefights.com/challenge/YeHucxXniMDZs2KAg #
"""
def DigitSumRange(a, b):
    res = 0
    for i in range(a, b + 1):
        while i > 0:
            res += i % 10
            i /= 10
    return res

DigitSumRange = lambda a,b: a > 0 and sum(sum(map(int,`i`)) for i in range(a, b + 1)) or  27 * b + 1

def DigitSumRange(a, b):
    s = lambda n: n > 0 and n % 10 + s(n / 10)
    
    r = 0
    while a <= b:
        r += s(a)
        a += 1
    return r