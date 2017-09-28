/*
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
 */
function decode2(message) {
    var res = '';
    for(var i = 0; i < message.length; i++) {
        var value = (message.charCodeAt(i) - 97 + 1) % 26;
        var newValue = (value * value + 25) % 26 + 97;
        res += String.fromCharCode(newValue);
    }
    
    return res;
}

function decode2(message) {
    var res = '';
    for(var i = 0; i < message.length; i++) {
        var value = (message.charCodeAt(i) - 97 + 1) % 26;
        var newValue = (value * value - 1) % 26 + 97;
        res += newValue != 96 ? String.fromCharCode(newValue):'z';
    }
    
    return res;
}