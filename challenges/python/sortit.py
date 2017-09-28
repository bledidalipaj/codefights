"""
You are given a string, your goal is to rearrange its letters in alphabetical order. If the same letter is 
present both in lowercase and uppercase forms in the initial string, the uppercase occurrence should go first 
in the resulting string.

Example

For str = "Vaibhav", the output should be
sortIt(str) = "aabhiVv".

[time limit] 4000ms (py)
[input] string str

A string consisting only of letters.

Constraints:
1 ≤ str.length ≤ 20

[output] string

# Challenge's link: https://codefights.com/challenge/KBmHkh6b7q68QBiHd/ #
"""
def sortIt(s):
	lower = []
	upper = []
	for char in s:
		if 'a' <= char <= 'z':
			lower.append(char)
		else:
			upper.append(char)
	return "".join(sorted(upper + lower, key=lambda s: s.lower()))

def sortIt(s):
	return "".join(sorted(sorted(s), key=lambda s: s.lower()))

def sortIt(s):
    cnt = [0] * 256
    for c in s:
        cnt[ord(c)] += 1
    res = ""
    for i in range(26):
        for j in range(cnt[ord('A') + i]):
            res += chr(ord('A') + i)
        for j in range(cnt[ord('a') + i]):
            res += chr(ord('a') + i)
    return res


sortIt = lambda s: "".join(sorted(s,key=lambda a: a.lower()+a))
sortIt = lambda S: `sorted(c.lower()+c for c in S)`[4::7]
sortIt = lambda S: "".join(sorted(c.lower()+c for c in S))[1::2]
sortIt = lambda s: ''.join(sorted(s, key=lambda x: (x.lower(), x)))