"""
I've learned some great coding tricks by looking at other users' challenge solutions, but the code 
is often very difficult to understand. The code golf scoring, which values using the minimum number 
of characters, often yields code that is difficult to read and maintain. To reach the lowest score, 
users name all methods and variables with one character. Sometimes users even choose a less efficient 
library method due to a shorter name.

A recent forum discussion suggested an alternate scoring method that doesn't punish the use of descriptive 
names. In this alternative method, all keywords and identifiers (variable names, class names, and function 
names) count as 1 point.

In this challenge, your task is to implement a function that will calculate the advanced score of a given 
code snippet written in JavaScript (ES6). The score of a snippet should be calculated using the following 
rules:

Language keywords and identifiers count as 1 point. A keyword or identifier is a word containing English 
letters and digits, with the first character being a letter.
Strings literals count as the full length of the string including the surrounding quotation marks. Both 
single (') and double (") quotes can be used. For the sake of simplicity, assume that string literals can't 
contain quotes.
Number literals count as the full length of the text representing the number.
Whitespace characters count as 0 points.
All other characters (e.g. ()[];:,.?<>\\/!@#$...) count as 1 point.
Assume that the code does not contain comments or regular expressions.
Given a valid JavaScript code snippet, calculate its score based on the rules above and return the score as 
an integer.

Example

For code = "var text = "This is JavaScript text";", the output should be
codeGolfReducedScore(code) = 29.

var is a keyword: 1 point;
text is an identifier: 1 point;
= is a non-whitespace character: 1 point;
"This is JavaScript text" is a string literal: 25 points;
; is a non-whitespace character: 1 points.
Thus, the total score is 1 + 1 + 1 + 25 + 1 = 29.

For code = "let date = Date.now();", the output should be
codeGolfReducedScore(code) = 9.

let = 1
date = 1
= = 1
Date = 1
. = 1
now = 1
(); = 3
1 + 1 + 1 + 1 + 1 + 1 + 3 = 9.

For code = "var test = '';\nfor (var index = 0; index < 10; index++)\ntest += index;\nalert(test);",
the output should be
codeGolfReducedScore(code) = 30.

var = 1
test = 1
= = 1
'' = 2
; = 1
for = 1
( = 1
var = 1
index = 1
= = 1
0 = 1
; = 1
index = 1
< = 1
10 = 2
; = 1
index = 1
++ = 2
) = 1
test = 1
+= = 2
index = 1
; = 1
alert = 1
( = 1
test = 1
); = 2
The total score is 30.

Input/Output

[time limit] 4000ms (py3)
[input] string code

A valid JavaScript (ES6) snippet with the restrictions given in the descriptions above.

Constraints:
10 ≤ code.length ≤ 400.

[output] integer

The number of points for the submitted code, given the scoring rules in the description above.

# Challenge's link: https://codefights.com/challenge/9kmuSXmkpwEpNLkYj/ #
"""
def codeGolfReducedScore(code):
    isToken = False
    curNum = 0
    curString = 0
    res = 0
    for ch in code:
        if isToken and not (ch.isalpha() or ch.isdigit()):
            isToken = False
            res += 1
        if curNum > 0 and not ch.isdigit():
            res += curNum
            curNum = 0
        if ch == '"' or ch == '\'' or curString > 0:
            curString += 1
            if curString > 1 and (ch == '"' or ch == '\''):
                res += curString
                curString = 0
        elif ch.isalpha():
            isToken = True
        elif ch.isdigit():
            if not isToken:
                curNum += 1
        elif not ch.isspace():
            res += 1
    if isToken:
        res += 1
    if curNum > 0:
        res += curNum
    return res