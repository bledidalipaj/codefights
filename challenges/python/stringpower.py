"""
This is a reverse challenge. Enjoy!

[time limit] 4000ms (py)
[input] string string1

An ASCII string.

Constraints:
1 ≤ string1.length ≤ 20.

[input] string string2

As ASCII string.

Constraints:
1 ≤ string2.length ≤ 20.

[output] integer

An integer.

Input:
string1: "a"
string2: "a"
Expected Output:
0

Input:
string1: "a"
string2: "b"
Expected Output:
1

Input:
string1: "ab"
string2: "ad"
Expected Output:
2

Input:
string1: "ab"
string2: "b"
Expected Output:
97

Input:
string1: "AbCefg"
string2: "gGJhh"
Expected Output:
80

# Challenge's link: https://codefights.com/challenge/yHk9jwKBFWCvNqyLR/main #
"""
def StringPower(string1, string2):
    s1 = sum(ord(char) for char in string1)
    s2 = sum(ord(char) for char in string2)
    return abs(s1 - s2)

StringPower = lambda string1, string2: abs(sum(map(ord, string1)) - sum(map(ord, string2)))