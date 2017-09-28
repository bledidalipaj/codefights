"""
This is a reverse challenge, enjoy!

Input/Output

[time limit] 4000ms (py3)
[input] string s

A string consisting of lowercase English letters.

Constraints:
0 ≤ string.length ≤ 5000.

[output] string

Input:
s: "a"
Output:
"0"
Expected Output:
"0"

Input:
s: "abc"
Output:
"3"
Expected Output:
"3"

Input:
s: "four"
Output:
"0"
Expected Output:
"0"

Input:
s: "fivec"
Output:
"22"
Expected Output:
"22"

Input:
s: "codewriting"
Output:
"323"
Expected Output:
"323"
"""
def alpha4(s):
    res = []
    for i in range(0, len(s), 4):
        val = 0
        for ch in s[i : i + 4]:
            val += ord(ch) - ord('a')
        res.append(str(val % 4))
    return ''.join(res)