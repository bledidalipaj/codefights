"""
Given an integer num, write an algorithm that determines if the given number has consecutive 1s in its binary representation.

Example

For num = 3, the output should be
consecutiveBit(num) = true.

310 is 112, which contains a pair of consecutive 1s.

For num = 21, the output should be
consecutiveBit(num) = false.

2110 is 101012, which contains no consecutive 1s.

Input/Output

[time limit] 4000ms (py)
[input] integer num

Constraints:
0 ≤ num < 231.

[output] boolean

Return true if the boolean representation of num contains consecutive 1s, otherwise return false.

# Challenge's link: https://codefights.com/challenge/fW66dxr49QERhv8KK #
"""
def consecutiveBit(num):
    prev = 0
    
    while num:
        if prev * num % 2 == 1:
            return True
        prev = num % 2
        num /= 2
    return False

consecutiveBit = lambda num: '11' in bin(num)
consecutiveBit = lambda n: n & n >> 1