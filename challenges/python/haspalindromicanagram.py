"""
A palindrome is a string that reads the same left-to-right and right-to-left. For example, "Madam, I'm Adam" and 
"Poor Dan is in a droop" are both palindromes. Note that letter case and non-alphanumeric characters should be ignored 
when deciding whether a string is a palindrome or not.

А string x is an anagram of another string y if you can obtain y by rearranging the letters of x. For example, "cinema" 
is an anagram of "iceman", and vice versa. Note that the string and its anagram must have the same length. By definition, 
the string is not considered as an anagram of itself. In anagrams, non-alphanumeric characters and letter case are important. 
For instance, "Oo" is not the same as "oO", making "Oo" an anagram of "oO" and vice versa.

Given a message, your task is to determine whether there is an anagram of the message that is also a palindrome.

Example

For message = "abab", the output should be
hasPalindromicAnagram(message) = true.

Among the anagrams of "abab", there are two strings that are also palindromes ("abba" and "baab"), so the answer is true.

For message = "bob", the output should be
hasPalindromicAnagram(message) = false.

The only rearrangement of the letters in the string "bob" that is a palindrome is the word itself, but this is not an anagram 
as defined above. Therefore, the answer is false.

For message = "heh!", the output should be
hasPalindromicAnagram(message) = true.

"!heh", "h!eh" and "he!h" are all palindromes and all of them are anagrams of "heh!". Remember that according to the rules laid 
out above, non-alphanumeric characters are ignored in palindromes but need to be considered in anagrams.

[time limit] 4000ms (py)
[input] string message

A string containing at least one alphanumeric character.

0 < message.length ≤ 20

[output] boolean

# Challenge's link: https://codefights.com/challenge/gRkR2xSSNnnAWADmj/ #
"""
def hasPalindromicAnagram(message):
    cnt = [0] * 36
    nonAlphanumeric = False
    for i in range(len(message)):
        if 'a' <= message[i] <= 'z':
            cnt[ord(message[i]) - ord('a')] += 1
        elif 'A' <= message[i] <= 'Z':
            cnt[ord(message[i]) - ord('A')] += 1
        elif '0' <= message[i] <= '9':
            cnt[ord(message[i]) - ord('0') + 26] += 1
        else:
            nonAlphanumeric = True
    odd = 0
    even = 0
    for i in range(36):
        if cnt[i] % 2 != 0:
            odd += 1
        elif cnt[i] > 0:
            even += 1
    return odd <= 1 and (even > 1 or nonAlphanumeric or even == 1 and message[::-1] != message)