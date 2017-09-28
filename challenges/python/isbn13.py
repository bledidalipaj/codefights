"""
The International Standard Book Number (ISBN) is a unique numeric commercial book identifier.

The ISBN is assigned to each edition and variation (except reprintings) of a book. For example, an e-book, a paperback 
and a hardcover edition of the same book would each have a different ISBN. The ISBN is 13 digits long if assigned on or 
after 1 January 2007, and 10 digits long if assigned before 2007.

Check out the link given above to read more about ISBN formats and their check digits.

You will be given an old ISBN-10 number with a wrong or absent check digit. Your mission is to calculate and fix it and 
return the fixed result along with ISBN-13 format.

The answer should thus be an array of two strings of the following formats:
["ISBN-10: x-xxx-xxxxx-x", "ISBN-13: xxx-x-xxx-xxxxx-x"].

Example

ISBN13("0-306-40615") = ["ISBN-10: 0-306-40615-2", "ISBN-13: 978-0-306-40615-7"].

ISBN13("0306406158") = ["ISBN-10: 0-306-40615-2", "ISBN-13: 978-0-306-40615-7"]

Input/Output

[time limit] 4000ms (py)
[input] string number

A string containing 9 to 10 digits and hyphens.

Constraints:
9 ≤ number.length ≤ 15.

[output] array.string

Two ISBN numbers in the format ["ISBN-10: x-xxx-xxxxx-x", "ISBN-13: xxx-x-xxx-xxxxx-x"].

# Challenge's link: https://codefights.com/challenge/P7YGDX6JWwzym93Qu #
"""
def ISBN13(number):
    isbn10_digits = map(int, re.findall(r'\d', number))
    
    # remove wrong check digit
    if len(isbn10_digits) == 10:
        isbn10_digits.pop()
    
    def isbn10_check_digit(isbn10):
        weighted_sum = 0
        for i in range(len(isbn10)):
            weighted_sum += (10 - i) * isbn10[i]
        
        check_digit = (11 - weighted_sum % 11) % 11
        if check_digit == 10:
            check_digit = 'X'
        return check_digit
    
    def isbn13_check_digit(isbn13):
        weighted_sum = 0
        for i in range(len(isbn13)):
            if i % 2 == 0:
                weighted_sum += 1 * isbn13[i]
            else:
                weighted_sum += 3 * isbn13[i]
        
        check_digit = (10 - (weighted_sum % 10)) % 10
        return check_digit
    
    isbn10_digits.append(isbn10_check_digit(isbn10_digits)) 
    isbn13_digits = [9, 7, 8] + isbn10_digits
    isbn13_digits.pop()
    isbn13_digits.append(isbn13_check_digit(isbn13_digits))
    
    isbn10 = '{}-{}{}{}-{}{}{}{}{}-{}'.format(*isbn10_digits)
    isbn13 = '{}{}{}-{}-{}{}{}-{}{}{}{}{}-{}'.format(*isbn13_digits)
    
    return ['ISBN-10: ' + isbn10, 'ISBN-13: ' + isbn13]
        
        