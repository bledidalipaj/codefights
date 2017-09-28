"""
Consider the following algorithm for the given positive integer n:

print n
if n = 1 then STOP;
if n is odd then 
n = 3 * n + 1
else
n = n / 2;
goto 2
For the given integer n, return the second largest value that will be printed by the algorithm above.

Example

For n = 22, the output should be
secondLargest(n) = 40.

The following values will be printed:
22 11 34 16 52 26 13 40 20 10 5 16 8 4 2 1.

The second largest number in this sequence is 40, which is the answer.

Input/Output

[time limit] 4000ms (py)
[input] integer n

An integer.

Constraints:
2 ≤ n ≤ 1000.

[output] integer

The second largest number that will be printed.

# Challenge's link: https://codefights.com/challenge/qQ762Pzrgm5KaBMT6/main #
"""

def secondLargest(n):
    seq = []
    
    while True:
        seq.append(n)
        if n == 1:
            break
        if n % 2 != 0:
            n = 3 * n + 1 
        else:
            n /= 2
    seq.sort()
    return seq[-2] if len(seq) >= 2 else seq[0]