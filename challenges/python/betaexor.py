"""
This is a reverse challenge, enjoy!

[time limit] 4000ms (py)
[input] string s

Constraints:
0 ≤ s.length ≤ 100.

[output] integer

Input:
s: "a"
Output:
Empty
Expected Output:
97

Input:
s: ""
Output:
Empty
Expected Output:
0

Input:
s: "CodeFight"
Output:
Empty
Expected Output:
121

Input:
s: "AAbbb"
Output:
Empty
Expected Output:
98

Input:
s: "Hint: This is a valid test! :-P"
Output:
Empty
Expected Output:
90

# Challenge's link: https://codefights.com/challenge/M8cR5yNub3PrwXkkp #
"""
def betaExor(s):
    res = 0
    for char in s:
        res ^= ord(char)
    return res

betaExor = lambda s: reduce(lambda x, y: x ^ ord(y), 0)