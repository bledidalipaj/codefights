"""
Run-length encoding (RLE) is a very simple form of lossless data compression in which runs of data 
(that is, sequences in which the same data value occurs in many consecutive data elements) are stored 
as a single data value and count, rather than as the original run.

Given a string s, your task is to encode it using the RLE.

Example

For s = "aabbbccc", the output should be
encode(s) = "a2b3c3".

Input/Output

[time limit] 4000ms (py3)
[input] string s

A string consisting of lowercase English letters.

Constraints:
1 ≤ s.length ≤ 104.

# Challenge's link: https://codefights.com/challenge/u48jf3T4spZ4J8aDg #
"""
def encode(s):
    ans = ''
    counter = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            ans += s[i - 1] + str(counter)
            counter = 1
    ans += s[-1] + str(counter)
    return ans