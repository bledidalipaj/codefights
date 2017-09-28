"""
An autogram is a sentence that describes itself in the sense of providing an inventory of its own characters. An essential 
feature is the use of full cardinal number names such as "one", "two", etc.

A special kind of autogram is a reflexicon (short for "reflexive lexicon"), which is a self-descriptive word list that describes 
its own letter frequencies.

Implement the Reflexicon function that returns true if the given sentence is a reflexicon and false otherwise.

Example

For

sentence = "sixteen e's, six f's, one g, three h's, nine i's, 
            nine n's, five o's, five r's, sixteen s's, five t's,
            three u's, four v's, one w, four x's"
the output should be
Reflexicon(sentence) = true.

There are indeed 16 'e's, 6 'f's, 3 'h's, 9 'i's, 9 'n's, 5 'o's, 5 'r's, 16 's's, 3 'u's, 4 'v's, 1 'w' and 4 'x's in the given sentence.

Input/Output

[time limit] 4000ms (py)
[input] string sentence

Each sentence consists of several phrases of format number letter['s], separated by ,. It is guaranteed that each number is in range [1, 19].

Constraints:
5 ≤ sentence.length ≤ 200.

[output] boolean

true if the sentence is a reflexicon and false otherwise.

# Challenge's link: https://codefights.com/challenge/KmevSoGg4zJKfJaHd #
"""
def Reflexicon(sentence):
    num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                'eleven': 11, 'twelve': 12, 'thirteen': 13,
                'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
                'eighteen': 18, 'nineteen': 19}
    phrases = sentence.split(',')
    
    for phrase in phrases:
        items = phrase.split()
        freq = num_dict[items[0]]
        letter = items[1][0]
        
        if sentence.count(letter) != freq:
            return False
    return True

def Reflexicon(sentence):
    nums = ['one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen',
                'fourteen', 'fifteen', 'sixteen', 'seventeen',
                'eighteen', 'nineteen']
    phrases = sentence.split(',')
    
    for phrase in phrases:
        items = phrase.split()
        freq = nums.index(items[0]) + 1
        letter = items[1][0]
        
        if sentence.count(letter) != freq:
            return False
    return True

def Reflexicon(sentence):
    nums = ['one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen']
    for token in sentence.split(', '):
        num, letter = token.split(' ')
        letter = letter[0]
        if nums.index(num) + 1 != sentence.count(letter):
            return False
    return True