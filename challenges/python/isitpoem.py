"""
You are given a poem text represented as an array of its lines. Let's assume that two lines rhyme if their last three letters are the same. 
Determine whether a given text is a poem with rhyming lines as specified by the rhyme array, such that its length divides the length of text.

rhyme specifies which lines should rhyme as follows: let the length of rhyme be M. For each i < M and j < M if rhyme[i] = rhyme[j], then the 
(i + k * M)th and the (j + k * M)th lines of the text should rhyme for any valid integer k.

Example

For
rhyme = [1, 2, 1, 2] and

text = ["When the moon skims the water", 
        "that sighs and shifts in its slumber", 
        "I wish it were still a quarter", 
        "to dial your number"]
the output should be
isItPoem(rhyme, text) = true.

The first line should rhyme with the third one, and the second line should rhyme with the fourth one.
"water" rhymes with "quarter and "slumber" rhymes with "number", so the answer is true.

For
rhyme = [2, 2] and

text = ["She'd swim in the oval", 
        "lake whose opal", 
        "mirror, framed by bracken", 
        "felt happy broken"]
the output should be
isItPoem(rhyme, text) = false.

The first line should rhyme with the second one, and the third line should rhyme with the last one.
But "oval" and "opal" differ in the third letter from the end ('v' and 'p').

Input/Output

[time limit] 4000ms (py)
[input] array.integer rhyme

A non-empty array of integers.

Constraints:
1 ≤ rhyme.length ≤ 10,
-1 ≤ rhyme[i] ≤ 45.

[input] array.string text

Array of strings that form a text. It is guaranteed that the last three characters of each string are letters.

Constraints:
2 ≤ text.length ≤ 10,
3 ≤ text[i].length ≤ 40.

[output] boolean

true if text is a poem and false otherwise.

# Challenge's link: https://codefights.com/challenge/kEidRSEGFw86GhRsu/main #
"""
def isItPoem(rhyme, text):
    M = len(rhyme)
    N = len(text)
    
    for i in range(M):
        for j in range(i + 1, M):
            if rhyme[i] == rhyme[j]:
                k = 0
                while i + k * M < N and j + k * M < N:
                    if text[i + k * M][-3:] != text[j + k * M][-3:]:
                        return False
                    k += 1
    return True