"""
Jack isn't really good at math, but his sadistic teacher still gave him some math exercises about sequences. He needs to find 
the next number of the given sequence, which can be one of the following three types:

arithmetic progression;
geometric progression;
pseudo-fibonacci sequence (a sequence each element of which is the sum of two preceding elements).
You are given 4 first numbers in the series as a string, in which the numbers are separated by commas. Help Jack to figure out 
what type of the sequence it is, and return the next number.

Example

For sequence = "4,6,10,16", the output should be
CompletetheSequence(sequence) = 26.

The sequence is a pseudo-fibonacci sequence.

For sequence = "5,10,20,40", the output should be
CompletetheSequence(sequence) = 80.

The sequence for a geometric progression with r = 2.

For sequence = "2,4,6,8", the output should be
CompletetheSequence(sequence) = 10.

The sequence for a arithmetic progression with d = 2.

Input/Output

[time limit] 4000ms (py3)
[input] string sequence

A string containing 4 numbers separated by a comma.

Constraints:
7 ≤ sequence.length ≤ 254.

[output] integer

The next element of the sequence.

# Challenge's link: https://codefights.com/challenge/QLdW6grw8hEr75tLu #
"""
def CompletetheSequence(sequence):
    sequence = map(float, sequence.split(','))
    
    if sequence[1] - sequence[0] == sequence[2] - sequence[1] == sequence[3] - sequence[2]:
        ans = sequence[-1] + sequence[1] - sequence[0]
    elif sequence[1] / sequence[0] == sequence[2] / sequence[1] == sequence[3] / sequence[2]:
        ans = sequence[-1] * (sequence[1] / sequence[0])
    else:
        ans = sequence[-1] + sequence[-2]
    return ans

# python3
def CompletetheSequence(sequence):
    sequence = list(map(int, sequence.split(',')))
    ln = len(sequence)
    
    if len(set([sequence[i] - sequence[i - 1] for i in range(1, ln)])) == 1:
        ans = sequence[-1] + sequence[1] - sequence[0]
    elif len(set([sequence[i] / sequence[i - 1] for i in range(1, ln)])) == 1:
        ans = ans = sequence[-1] * (sequence[1] / sequence[0])
    else:
        ans = sequence[-1] + sequence[-2]
    return ans

def CompletetheSequence(sequence):
    nums = list(map(int, sequence.split(',')))
    if nums[1] - nums[0] == nums[2] - nums[1] == nums[3] - nums[2]:
        return nums[3] + nums[1] - nums[0]
    if nums[1] ** 2 == nums[0] * nums[2] and nums[2] ** 2 == nums[1] * nums[3]:
        return nums[3] * nums[3] / nums[2]
    return nums[2] + nums[3]

def CompletetheSequence(s):
    a, b, c, d = map(int, s.split(','))
    
    e = 2 * d - c
    
    if b + c == d:
        e = c + d
    elif c * c  == d * b:
        e =  d * d / c
    return e