"""
Pick a positive integer, write it out in English words, then count the total number of letters in 
the words. Keep repeating this process using the total as the new number to write and eventually you 
will reach an infinite loop at the number 4, no matter which number you start from.

Your task is to find the number of steps it takes to reach the number 4 from the given integer n.

Here are some examples of how numbers should be written and counted:

1 = one (3 letters)
14 = fourteen (8 letters)
30 = thirty (6 letters)
42 = forty two (8 letters)
216 = two hundred sixteen (17 letters)
1500 = one thousand five hundred (22 letters)
1000000 = one million (10 letters)
987654321 = nine hundred eighty seven million six hundred fifty four thousand three hundred twenty one (77 letters)
Example

For n = 377, the output should be
NumberOfLetters(n) = 5.

377 would be written as three hundred seventy seven which has 24 letters.
24 would be written as twenty four which has 10 letters.
10 would be written as ten which has 3 letters.
3 would be written as three which has 5 letters.
5 would be written as five which has 4 letters.
We have now reached 4 and there were 5 steps in total, so the result is 5.

Input/Output

[time limit] 4000ms (py)
[input] integer n

The starting number.

Constraints:
0 < n < 109

[output] integer

The number of steps taken to reach 4 from n.

# Challenge's link: https://codefights.com/challenge/wcNrgbtmpWWn4DTwu #
"""
def NumberOfLetters(n):
	pass

def NumberOfLetters(n):
    max_ordermag = 9 #Constraints n to between 0 and 10^(value)
    if (n > 10**max_ordermag) or (n < 0):
        print("Invalid input\n")
        return None
    
    str_big = {2:'hundred', 1: 'thousand', 0: 'million'}
    str_singledigit = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 
                        5: 'five', 6: 'six', 7: 'seven', 
                        8: 'eight', 9: 'nine'}
    str_teens = {11: 'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 
                 16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    str_tens = {1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',
                7:'seventy',8:'eighty',9:'ninety'}
    
    def NumberToString(k):
        ''' 0 < k < 1000 '''
        hundred = (k - (k % 100)) // 100
        if hundred < 0:
            hundred = 0
        
        #First if clause handles cases like k = 216, where the last two digits are in the teens
        if (k - 100*hundred) > 10 and (k - 100*hundred) < 20:
            single = k - 100*hundred
            ten = 0
        else:
            ten = (k - 100 * hundred) // 10
            if ten < 0:
                ten = 0
                single = (k - hundred*100 - ten*10)
            elif (ten < 20) and (ten > 10): #larger than 0, but need special treatment
                single = ten 
                ten = 0
            else:
                single = (k - hundred*100 - ten*10)
                
        output_str = ''
        if (hundred > 0):
            output_str += str_singledigit[hundred]+'hundred'
        if (ten > 0):
                output_str += str_tens[ten]
        if (single > 0):
            if (single > 10) and (single < 20):
                output_str += str_teens[single]
            else:
                output_str += str_singledigit[single]
    
        return(output_str)
    
    #Construct a list that records the order of magnitude of temp_int
    #[millions, thousands, hundreds]
    iterations = 0
    temp_int = n
    list_ordermag = []
    
    while temp_int != 4:
        iterations += 1
        for i in (6,3,2):
            if (temp_int % (10**i)) == temp_int:
                list_ordermag.append(0)
            else:
                if (i == 6):
                    list_ordermag.append(temp_int // (10**i))
                elif (i == 3):
                    list_ordermag.append( (temp_int // (10**i)) % 1000)
                elif (i == 2):
                        list_ordermag.append( (temp_int // (10**i) % 10) )
                            
        output_str = ''
        for j in range(len(list_ordermag)):
            if list_ordermag[j] != 0:
                output_str += NumberToString(list_ordermag[j]) + str_big[j]
        output_str += NumberToString(temp_int - 10**6 * list_ordermag[0] - 
                                     10**3 * list_ordermag[1] -
                                     10**2 * list_ordermag[2])
        temp_int = len(output_str)
        list_ordermag = []

    return(iterations)