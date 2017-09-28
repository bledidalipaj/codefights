"""
Morse code is a method of transmitting text information as a series of on-off tones, lights, or clicks. For more information, please read here.

Many of you might have watched a great movie called "The Imitation Game". For those of you who haven't, the movie is about cracking the enigma code 
during the WWII. In this challenge you're facing a similar problem.

You will be provided the encrypted message in International Morse Code and the encrypted key, which is a code of the "CF" message. Your mission is to 
build the correct code table and decrypt the message.

Please note that we will use "." for dot and "_" for dah.

Space between letters: 1
Space between words: 2
Example

For message = "_._. ___ _.. . .._. .. __. .... _ ..." and
key = "_._. .._.", the output should be
MorseCode(message, key) = "CODEFIGHTS".

The key stands for the original Morse table, so the message can be decrypted right away. The encrypted message is "CODEFIGHTS".

Input/Output

[time limit] 4000ms (py)
[input] string message

The encrypted message, a string consisting of symbols '_', '.' and ' '. It is guaranteed that the message is written in a correct Morse Code.

Constraints:
1 ≤ message.length ≤ 100.

[input] string key

The key to the Morse Table, a string consisting of symbols '_', '.' and ' '. The key is guaranteed to correctly represent two symbols (C and F) written 
in Morse Code.

Constraints:
1 ≤ key.length ≤ 20.

[output] string

Decrypted message consisting of uppercase English letters 'A'-'Z'.

# Challenge's link: https://codefights.com/challenge/ybZTsJspbK9u8iKZb #
"""
def MorseCode(message, key):
    morse = [
        "._",
        "_...", 
        "_._.",
        "_..",
        ".",
        ".._.",
        "__.",
        "....",
        "..",
        ".___",
        "_._",
        "._..",
        "__",
        "_.",
        "___",
        ".__.",
        "__._",
        "._.",
        "...",
        "_",
        ".._",
        "..._",
        ".__",
        "_.._",
        "_.__",
        "__.."
    ]
    
    C, F = key.split(" ")
    shift = (morse.index(C) - morse.index("_._.")) % 26
    
    decoded_message = []
    
    for word in message.split("  "):
        decoded_chars = []
        for char in word.split(" "):
            index = (morse.index(char) - shift) % 26
            decoded_chars.append(chr(ord("A") + index))
        decoded_message.append("".join(decoded_chars))
    return " ".join(decoded_message)