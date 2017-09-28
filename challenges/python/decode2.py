"""
A squared encoding in a simple encoding algorithm that can be used to encrypt messages of moderate importance. To encrypt a message 
consisting of lowercase English letters, the following steps should be taken:

consider message characters one by one;
each letter is assigned to a number: 'a' to 1, 'b' to 2, and so on, with 'y' assigned to 25 and 'z' assigned to 0;
take a value assigned to the character, calculate its square modulo 26, and add the letter assigned to the obtained result to the answer.
Given a message, your task is to encode it using the squared encoding algorithm.

Example

For message = "hello", the output should be
decode2(message) = "lynnq".

Here's why:

'h' -> 82 % 26 = 64 % 26 = 12 -> 'l';
'e' -> 52 % 26 = 25 % 26 = 25 -> 'y';
'l' -> 122 % 26 = 144 % 26 = 14 -> 'n';
'o' -> 152 % 26 = 225 % 26 = 17 -> 'q'.
Input/Output

[time limit] 4000ms (py3)
[input] string message

A string consisting of lowercase English letters.

Constraints:
1 ≤ message.length ≤ 100.

[output] string

Squared encoded message.

# Challenge's link: https://codefights.com/challenge/6FcoYgXWmxETjuuaj #
"""
def decode2(message):
    numLetterDict = {(c + 1) % 26:chr(c + ord('a')) for c in range(26)}
    letterNumDict = {chr(c + ord('a')): (c + 1) % 26 for c in range(26)}
    encodedMessage = ''
    
    for char in message:
        value = letterNumDict[char]
        encodedMessage += numLetterDict[(value * value) % 26]
    return encodedMessage

def decode2(message):
    res = ''
    
    for char in message:
        value = (ord(char) - ord('a') + 1) % 26
        res += chr((value * value - 1) % 26 + ord('a'))
    return res

decode2 = lambda message: "".join(chr((((ord(char) - 96) % 26) ** 2 - 1) % 26 + 97) for char in message)