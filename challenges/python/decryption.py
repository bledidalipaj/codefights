"""
This is a reverse challenge, enjoy!

[time limit] 4000ms (py)
[input] array.integer bytelist
[output] string

Input:
bytelist: [97]
Expected Output:
"a"

bytelist: [97, 97, 0, 0, 0, 0, 0, 0, 0, 0]
Expected Output:
"aaaaaaaaaa"

Input:
bytelist: [97, 98, 2]
Expected Output:
"abc"

Input:
bytelist: [104, 101, 4, 7, 3, 52, 8, 79, 123, 125, 114]
Expected Output:
"hello world"

# Challenge's link: https://codefights.com/challenge/28tzsTCcFaomnxZKC #
# Caesar cypher -> https://inventwithpython.com/chapter14.html
"""
def decryption(bytelist):
    ln = len(bytelist)
    
    if ln < 2:
        msg = [bytelist[0]]
    else:
        msg = [bytelist[0], bytelist[1]]
        
    for i in range(2, ln):
        msg.append((bytelist[i] + msg[i - 2]) % 128)
    return "".join(map(chr, msg))