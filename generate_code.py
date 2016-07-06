"""
Your task is to implement a function that generates automobile codes by their label, year, model and number. The code should have format 
<l><y><m><num>, where:

<l> is a label;
<y> consists of last to digits of year, or equals 0year, if year has only one digit;
<m> is a number that can be determined from model, a character in range 'A' - 'L';
<num> is a number formatted so that the length of the code is 9 digits, i.e. it should either be truncated to its last digits, or be 
preceded by '0's.
Example

For label = "B", year = 2015, model = 3 and number = 678,
the output should be
GenerateCode(label, year, model, number) = "B15C00678".

In this example, number should be preceded by '0's.

For label = "XYZ", year = 2017, model = 9 and number = 10000,
the output should be
GenerateCode(label, year, model, number) = "XYZ17I000".

Here number is too long, so only its last 3 digits are taken.

For label = "ABCD", year = 1, model = 10 and number = 8799,
the output should be
GenerateCode(label, year, model, number) = "ABCD01J99".

In this example year is written as 01 because it consists of a single digit, and number is truncated to last two digits.

Input/Output

[time limit] 4000ms (py)
[input] string label

A string of uppercase English letters.

Constraints:
1 ≤ label.length ≤ 5.

[input] integer year

Constraints:
1 ≤ year < 104.

[input] integer model

Constraints:
1 ≤ model ≤ 12.

[input] integer number

Constraints:
1 ≤ number ≤ 104.

[output] string

A string of length 9, automobile code.

# Challenge's link: https://codefights.com/challenge/GPw6LZT685xxJgnvT/main #
"""
def GenerateCode(label, year, model, number):
    code = []
    length = 0
    
    # first step
    code.append(label)
    length += len(label)
    
    # second step
    if year < 9:
        code.append('0' + str(year))
    else:
        code.append(str(year)[-2:])
    length += 2
    
    # third step
    code.append(chr(ord('A') + model - 1))
    length += 1
    
    # forth step
    number = '0' * 9 + str(number)
    code.append(number[length - 9:])
    return ''.join(code)