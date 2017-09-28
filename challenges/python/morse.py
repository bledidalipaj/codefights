"""
Probably the most well known Morse Code message is SOS.
The message is made up of three short signals, then three long signals, and then three short signals again (...---...). This is the 
distress signal that people send out when they need help.

According to Wikipedia, some historians have called the Morse code the first digital code. This is because the Morse code uses just 
two states (On and Off) that is to flicker the light on/off, turn the sound tone on/off, or analogically set electrical pulse high/low.

To conform to ITU standard, the basic transmission of Morse code must obey the following rules where 1 is On and 0 is Off:

Dot: the signal must be turn on for 1, i.e. 1;
Dash: the signal must be turn on for 3 time units long: 111;
The signal forming the same letter between the dots and dashes should be turned off for 1 time unit long: 0
         Example:       Letter 'X' = '-..-' the signal would be sent as
                                                    '11101010111'

Gap between letters: the signal should be turned off for 3 time units long: 000
         Example:       Word 'MR' = '-- .-.' the signal would be sent as
                                                       '11101110001011101'
                                                                 M                     R

Medium gap between words: the signal should be turned off for 7 times unit long: 0000000
         Example:       Messge 'MR X' = '-- .-. / -..-' the signal would be sent as
                                                               '11101110001011101000000011101010111'

Here's your task. Given the signal string, decode it into a text message if it represents a Morse-decoded text, or encode it with Morse code 
if it represents a regular text.

Check out this link for the reference: Internations Morse Code.

Hope this challenge will not make you send out the distress SOS signals.
Good Luck and have fun!

Example

For signal = "MR X", the output should be
communicateByMorse(signal) = "11101110001011101000000011101010111".

For signal = "11101110001011101000000011101010111",
the output should be
communicateByMorse(signal) = "MR X".

Input/Output

[time limit] 4000ms (py)
[input] string signal

A string that contains either Morse binary digital code ('0's and '1's) or a regular message (Uppercase Latin letters 'A'-'Z').

Constraints:
4 ≤ input.length ≤ 5000.

[output] string

The decoded/encoded signal.

# Challenge's link: https://codefights.com/challenge/8cmFKwcZYgc3LErHL/main #
"""
def communicateByMorse(signal):
    space_between_letters = 3
    space_between_words = 7
    
    d = ["10111", "111010101", "11101011101", "1110101", "1", 
         "101011101", "111011101", "1010101", "101", "1011101110111",
         "111010111", "101110101", "1110111", "11101", "11101110111",
         "10111011101", "1110111010111", "1011101", "10101", "111",
         "1010111", "101010111", "101110111", "11101010111", "1110101110111", "11101110101"]
    
    def encode_message(msg):
        res = []
        
        for i in range(len(msg)):
            char = msg[i]
            
            if "A" <= char <= "Z":
                res.append(d[ord(char) - ord("A")])
                res.append(space_between_letters * "0")
            else:
                res.pop()
                res.append(space_between_words * "0")
        res.pop()
        return "".join(res)
    
    def get_token(start, msg):
        end = start
        consecutive_zeros = 0
        if msg[start] == '1':
            while consecutive_zeros < 2 and end < len(msg):
                if msg[end] == '1':
                    consecutive_zeros = 0
                else:
                    consecutive_zeros += 1
                end += 1
            if consecutive_zeros == 2:
                end -= 2
        else:
            while msg[end] == '0' and end < len(msg):
                end +=   1
        return msg[start: end]
        
    def decode_message(msg):
        encoded_message = ""
        index = 0
        while index < len(msg):
            token = get_token(index, msg)
            
            if token in d:
                encoded_message += chr(ord("A") + d.index(token))
            elif token == "0" * space_between_words:
                encoded_message += " "
                
            index += len(token)
        return encoded_message
            
    if signal.isdigit():
        return decode_message(signal)
    return encode_message(signal)
        
         
    
    

## Second Solution
def communicateByMorse(code):
    morse = ["10111", "111010101", "11101011101", "1110101", "1", "101011101",
             "111011101", "1010101", "101", "1011101110111", "111010111", 
             "101110101", "1110111", "11101", "11101110111", "10111011101",
             "1110111010111", "1011101", "10101", "111", "1010111",
             "101010111", "101110111", "11101010111", "1110101110111", "11101110101"]
    rev_morse = {x: chr(i + ord('A')) for i, x in enumerate(morse)}
    if code[0].isdigit():
        words = code.split('0' * 7)
        decoded_words = []
        for word in words:
            chars = word.split('0' * 3)
            decoded_chars = []
            for char in chars:
                decoded_chars.append(rev_morse[char])
            decoded_words.append(''.join(decoded_chars))
        return ' '.join(decoded_words)
    else:
        words = code.split(' ')
        encoded_words = []
        for word in words:
            encoded_chars = []
            for char in word:
                encoded_chars.append(morse[ord(char) - ord('A')])
            encoded_words.append('000'.join(encoded_chars))
        return '0000000'.join(encoded_words)

## Third Solution
morse ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--.."
        }
morse_inverse = {v:k for k,v in morse.iteritems()}

def communicateByMorse(signal):
    if any( k in signal for k in morse ):
        return "0000000".join("000".join( "0".join( '111' if x=='-' else '1' for x in morse[letter] ) for letter in word ) for word in signal.split())
    else:
        ans = []
        for word in signal.split('0000000'):
            buf = ''
            for letter in word.split('000'):
                cur = ''
                for mesh in letter.split('0'):
                    cur += '-' if len(mesh) == 3 else '.'
                buf += morse_inverse[cur]
            ans.append(buf)
        return " ".join(ans)