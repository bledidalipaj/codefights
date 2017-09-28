"""
Sometimes, to make an on-line conversation more expressive, we use some smileys (or emoticons) in our messages.
 What actually happens is this: we use some notations that represent emoticons, and the chat system converts them 
 into images one a message is sent.

To replace a keyword with an emoticon, the system needs to correctly detect it first. Your mission is to write a 
function that will detect emoticons in a message. Given a message and emoticons, the function should detect all 
emotions in the message and enclose each of them in a pair of brackets ([ and ]).

Remember this: an emotion should be replaced only if it is indeed an emoticon, i.e. if it is a word that is not a 
part of some other word. Thus, the function shouldn't detect non-emoticons and ruin messages like in the image below:
code in Skype

Good luck, :P :D ;)

Example

For message = "I love you <3" and emoticons = ["<3", ":)", "^_^"],
the output should be
Emojticon(message) = "I love you [<3]".

<3 in the given message is, indeed, an emoticon.

For message = "I love you because 1<3" and
emoticons = ["<3", ":)", "^_^"], the output should be
Emojticon(message) = "I love you because 1<3".

Here <3 is not an emoticon, so it shouldn't be replaced.

Input/Output

[time limit] 4000ms (py)
[input] string message

A messages in the conversation.

Constraints
1 ≤ message.length ≤ 100.

[input] array.string emoticons

A set of emoticons that should be replaced. It is guaranteed that the emoticons are unique, and that no emoticon is a 
substring of another emoticon.

Constraints:
1 ≤ emoticons.length ≤ 10,
1 ≤ emoticons[i].length ≤ 5.

[output] string

The message with emoticons enclosed in brackets.


# Challenge's link: https://codefights.com/challenge/zwoGe7JRnS43tSbvm #
"""
def Emojticon(message, emoticons):
    word = ''
    newMessage = []
    for char in message:
        if char != ' ':
            word += char 
        else:
            if len(word) > 0:
                if word in emoticons:
                    word = '[' + word + ']'
                newMessage.append(word)
            newMessage.append(' ')
            word = ''
    if word in emoticons:
        newMessage.append('[' + word + ']')
    else:
        newMessage.append(word)
    return "".join(newMessage)