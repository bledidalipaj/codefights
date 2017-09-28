"""
Given an integer n, count the number of groups of consecutive 1 bits in its binary representation.

Example

For n = 1259, the output should be
GroupedBits(n) = 4.

The binary representation of 1259 is 10011101011, with the groups in bold.

Input/Output

[time limit] 4000ms (py)
[input] integer n

Constraints:
0 ≤ n ≤ 109.

[output] integer

The number of groups of 1 bits.

# Challenge'e link: https://codefights.com/challenge/YuBsjap3TBQN42nLk/main #
"""
def GroupedBits(n):
    res = 0
    count = True
    for bit in bin(n):
        if count and bit == '1':
            res += 1
            count = False
        if bit == '0':
            count = True
    return res

GroupedBits = lambda n: bin(2*n).count("10")
GroupedBits = lambda n: len(re.findall('1+',bin(n)))
GroupedBits = lambda n: re.subn('1+0*','',bin(n))[1]
GroupedBits = lambda n: n and n % 2 + GroupedBits(n - 1 & ~n - n)