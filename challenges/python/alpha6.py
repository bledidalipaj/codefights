"""
This is a reverse challenge. Enjoy!

Input:
s: "a"
Output:
Empty
Expected Output:
97

Input:
s: "cdefg"
Output:
Empty
Expected Output:
99

Input:
s: "abcdef"
Output:
Empty
Expected Output:
199

Input:
s: "CodeFights is about improving your coding skills by solving programming challenges."
Output:
Empty
Expected Output:
1716

# Challenge's link: https://codefights.com/challenge/nx6gxeSWryGgdrMaP #
"""
def alpha6(s):
	pass

alpha6 = lambda s: sum(map(ord,s[::5]))

def alpha6(s):
   out = 0
   for c in s[::5]:
       out += ord(c)
   return out