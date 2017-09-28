"""
You are given a string s that consists of English letters, punctuation marks, whitespace characters and brackets. It 
is guaranteed that the brackets in s form a regular bracket sequence.

Your task is to reverse the strings in each pair of matching parenthesis, starting from the innermost one.

Example

For string "s = a(bc)de" the output should be
reverseParentheses(s) = "acbde".

Input/Output

[time limit] 4000ms (py)
[input] string s

A string consisting of English letters, punctuation marks, whitespace characters and brackets. It is guaranteed that parenthesis 
form a regular bracket sequence.

Constraints:
5 ≤ x.length ≤ 55.

[output] string

# Challenge's link: https://codefights.com/challenge/Wg7u4KrHsYbZqvDar #
"""
def reverseParentheses(s):
	pass


def reverseParentheses(string):
    str_list = []

    for letter in string:
        print letter
        print str_list

        if letter == ")":
            sub_str_list = []

            parsed_letter = str_list.pop()
            while parsed_letter != "(":
                sub_str_list.append(parsed_letter)
                parsed_letter = str_list.pop()

            for element in sub_str_list:
                str_list.append(element)

        else:
            str_list.append(letter)

    return "".join(str_list)