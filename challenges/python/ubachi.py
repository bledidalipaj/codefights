"""
During World War I, the Germans used a double columnar transposition cipher called ubchi. To encrypt a certain message with 
ubchi, one should write it out in rows of a fixed length, and then read out again column by column in specific order. The 
process should be repeated a second time to ensure safe encryption.

Both the width of the rows and the permutation of the columns are usually defined by a keyword. For example, let the keyword 
be "pancake" (a word of length 7). The permutation is then defined by the alphabetical order of the letters in the keyword, 
i.e. 7, 1, 6, 3, 2, 5, 4 (note that that if the keyword has two equal letters, their order is defined by their order in the keyword).

Let the message to be encrypted be "target acquired. Successful extermination". When written out in columns, the following can be obtained:

7163254
target 
acquire
d. Succ
essful 
extermi
nation 
The columns should be rearranged to obtain the following rectangle:

1234567
aeg trt
ciuerqa
.uScc d
suf lse
xreimte
aoi ntn
This rectangle produces the following string: "ac.sxaeiuuroguSfei ec i trclmnrq stttadeen".

The process should be repeated again with the following results:

7163254        1234567
ac.sxae        cxsea.a
iuurogu        uorugui
Sfei ec  --->  f iceeS
 i trcl        irtlc  
mnrq st        n qtsrm
ttadeen        tedneat
The resulting encrypted string is thus "cufintxo r esritqdeucltnagecse.ue raaiS mt".

Given encrypted message and the keyword, your task is to decrypt it and return the original message.

Example

For message = "cufintxo r esritqdeucltnagecse.ue raaiS mt"
and keyword = "pancake", the output should be
Ubachi(message, keyword) = "target acquired. Successful extermination ".

This example corresponds to the example given in the description above. Note, that it has a whitespace character at the end: that is 
because the encryption requires a message that can be written out in a rectangle.

Input/Output

[time limit] 4000ms (py)
[input] string message

A message encrypted with ubachi encryption.

Constraints:
keyword.length ≤ message.length ≤ 120.

[input] string keyword

A keyword representing ubachi transposition key. It is guaranteed to contain only lowercase English letters.

Constraints:
3 ≤ keyword.length ≤ message.length.

[output] string

Decoded message.

# Challenge's link: https://codefights.com/challenge/WbDRnJGc7TYLdtkcp/ #
"""
def Ubachi(message, keyword):
    def encode(message, permutation, transpose=False):
        if len(message) % len(permutation) != 0:
            message += ' ' * (len(permutation) - len(message) % len(permutation))
        n, m = len(message) / len(permutation), len(permutation)

        trans_matrix = [[None] * m for _ in range(n)]
        for i, ch in enumerate(message):
            if transpose:
                trans_matrix[i % n][i / n] = ch
            else:
                trans_matrix[i / m][i % m] = ch
        res = [[None] * m for _ in range(n)]
        for i, pos in enumerate(permutation):
            for j in range(n):
                res[j][pos] = trans_matrix[j][i]
        if transpose:
            ans = ''.join(''.join(x) for x in res)
        else:
            ans = []
            for j in range(m):
                for i in range(n):
                    ans.append(res[i][j])
            ans = ''.join(ans)
        return ans

    s = list(sorted((ch, i) for i, ch in enumerate(keyword)))
    order = [0] * len(keyword)
    for i, el in enumerate(s):
        order[el[1]] = i
    reverse_order = [None] * len(order)
    for i, pos in enumerate(order):
        reverse_order[pos] = i
    return encode(encode(message, reverse_order, True), reverse_order, True)