"""
Your boss likes to prank you by sending you the sentence he wants to say as a list of words, with each word given as a 
list of characters. You are already tired of a such low level prank, and decide to write a program that would turn the 
sentences your boss sends to you into a readable form.

Remember to put a space between two words and put a period in the end of the sentence. Your boss is weird but kind enough 
not to send you sentences with other punctuation.

Note: if you want an additional challenge, try solving this challenge locally without using STL and C Runtime Library with 
the only exception being malloc(). Therefore the function you should the implement has the following format:

char* MakeSentence(char* words[])
{
    // function body
}
Example

For

words = [["G","o","o","d"], 
         ["m","o","r","n","i","n","g"]]
the output should be
makeSentence(words) = "Good morning.".

Input/Output

[time limit] 4000ms (py)
[input] array.array.char words

An array of words, each word is an array of characters.

Constraints:
1 ≤ words.length ≤ 10,
1 ≤ words[i].length ≤ 10.

[output] string

The output sentence after putting all the words together.

# Challenge's link: https://codefights.com/challenge/XLwudJsZ6JQR2a9uo #
"""
def makeSentence(words):
    for i in range(len(words)):
        words[i] = "".join(words[i])
        
    sentence = " ".join(words) + "."
    return sentence

def makeSentence(words):
    return " ".join(["".join(word) for word in words]) + "."

makeSentence = lambda words: ' '.join(map(''.join, words)) + '.'