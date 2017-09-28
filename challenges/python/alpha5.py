"""
This is a reverse challenge. Enjoy!

[time limit] 4000ms (py3)
[input] string s

A string consisting of lowercase English letters.

Constraints:
s.length = 5.

[output] char

An uppercase English letter.

# Challenge's link: https://codefights.com/challenge/KQqMrjTTZ3o8tASdP/solutions/3LfbeXBbSb7a6Jivw #

Input:
s: "aaaaa"
Output:
"R"
Expected Output:
"A"

Input:
s: "caaaa"
Output:
"T"
Expected Output:
"C"

Input:
s: "ababa"
Output:
"C"
Expected Output:
"C"

Input:
s: "abcde"
Output:
"K"
Expected Output:
"K"

Input:
s: "baaaz"
Output:
"A"
Expected Output:
"A"

Input:
s: "codef"
Output:
"C"
Expected Output:
"C"

Input:
s: "about"
Output:
"C"
Expected Output:
"C"

Input:
s: "phone"
Output:
"B"
Expected Output:
"B"
"""
def alpha5(s):
    total = sum(ord(char) for char in s)
    return chr(ord('A') + total % 485 % 26)
    

alpha5 = lambda s: chr(65 + sum(ord(c) for c in s) % 485 % 26)

alpha5=lambda s: chr(sum(map(ord, s),9)%26+65)

# map ord s gives list of charactervalues, -97 each to set 'a' to 0 is mod 26 the same as +7 each, 
# +5*7 is mod 26 the same as +9, %26 to stay within 0-25, +65 to go to 'A',chr to get the charvalue

alpha5 = lambda s: chr((sum(map(ord, s)) + 9) % 26 + 65)