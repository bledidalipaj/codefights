"""
Given a string that represents a linear algebraic expression, invert each plus or minus sign that is outside of 
any brackets in the expression.

Note that:

There can be three types of brackets in the expression: round (around me), curly {around me} or square [around me].
The expression will only contain plus and minus signs. There will not be any multiplication or division signs.
The only operands in the expression are variables, so the expression will not contain any numbers.
Each variable can be represented by an arbitrary number of consecutive characters.
The first variable in the input might not have a sign in front of it. In this case, the sign is assumed to be a plus 
sign.
In the output, there should be a sign in front of each variable, including the first one.
Brackets can form nested constructions of any depth. Brackets of a certain type can contain brackets of the same type 
inside (e.g. (...(...)...)). In addition, the order of nesting is not fixed (so both (...{...}...) and {...(...)...} 
are equally possible).
Example:

For linEq = "a + b - (c + d - {e})", the output should be
switchDemSigns(linEq) = "- a - b + (c + d - {e})".

Explanation:

a is outside all of the expression's brackets and does not have a sign in front of it, so it is considered positive in the 
input. Inverting the sign produces - a in the output.
b is also outside all of the brackets and has a plus sign in front of it, so it should be changed to - b in the output.
The sign right before (c + d - {e}) is negative, so we should put a plus sign there in the output.
All the other signs are inside the brackets, so they remain untouched.
[time limit] 4000ms (py)
[input] string linEq

Constraints:
linEq.length ≤ 150

[output] string

# Challenge's link: https://codefights.com/challenge/CHajJHHfGYuGKMW7D #
"""
def switchDemSigns(linEq):
    linEq = list(linEq)
    brackets = []
    
    for i in range(len(linEq)):
        if not brackets:
            if linEq[i] == '+':
                linEq[i] = '-'
            elif linEq[i] == '-':
                linEq[i] = '+'
            
        if linEq[i] in '(){}[]':
            if linEq[i] in  '({[':
                brackets.append(linEq[i])
            else:
                brackets.pop()
        
    if not linEq[0].startswith('-') and not linEq[0].startswith('+'):
        linEq.insert(0, '- ')
    return "".join(linEq)

def switchDemSigns(linEq):
    linEq = list(linEq)
    brackets = []
    
    for i in range(len(linEq)):
        if not brackets:
            if linEq[i] == '+':
                linEq[i] = '-'
            elif linEq[i] == '-':
                linEq[i] = '+'
            
        if linEq[i] in '(){}[]':
            if linEq[i] in  '({[':
                brackets.append(linEq[i])
            else:
                brackets.pop()
        
    if not (linEq[0].startswith('-') or linEq[0].startswith('+')):
        linEq.insert(0, '- ')
    return "".join(linEq)

def closestSequence(a, b):
    bestDiff = -1
    maskBound = 1 << len(b)

    for mask in range(maskBound):
        diff = 0
        curPos = 0
        for i in range(len(a)):
            if (mask & (1 << i)) != 0:
                diff += abs(a[curPos] - b[i])
                curPos += 1
                if curPos == len(a):
                    break
        if curPos == len(a) and (bestDiff == -1 or diff < bestDiff):
            bestDiff = diff

    return bestDiff