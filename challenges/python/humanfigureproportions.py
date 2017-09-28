"""
Here is what Leonardo da Vinci wrote on proportions of a human figure:

From the chin to the roots of the hair is 1/10 of the whole figure. From the joint of the palm of the hand to the 
tip of the longest finger is 1/10. From the chin to the top of the head 1/8; and from the pit of the stomach to the 
top of the breast is 1/6, and from the pit below the breast bone to the top of the head 1/4. From the chin to the nostrils 1/3...

You've discovered a manuscript containing the following text:

The whole figure is <number> inches. From the chin to the roots of the hair is <number> inches. From the joint of the 
palm of the hand to the tip of the longest finger is <number> inches. From the chin to the top of the head <number> 
inches; and from the pit of the stomach to the top of the breast is <number> inches, and from the pit below the breast 
bone to the top of the head <number> inches. From the chin to the nostrils <number> inches...

, where each <number> is either a positive integer or an ellipsis (...). Using proportions given in Leonardo's text, 
try to replace all <number>s with proper values. If the given text contains parts that contradict each other, return 
"Error" instead. It is guaranteed that if correct substitution exists, then ... correspond to some integer values.

Example

For

text = "The whole figure is ... inches.
  From the chin to the roots of the hair is 12 inches.
  From the joint of the palm of the hand to the tip of 
  the longest finger is ... inches. From the chin to
  the top of the head 15 inches; and from the pit of the stomach 
  to the top of the breast is ... inches, and from the pit below 
  the breast bone to the top of the head ... inches. 
  From the chin to the nostrils 40 inches..."
, the output should be

humanFigureProportions(text) = 
 "The whole figure is 120 inches. 
  From the chin to the roots of the hair is 12 inches. 
  From the joint of the palm of the hand to the tip of 
  the longest finger is 12 inches. From the chin to 
  the top of the head 15 inches; and from the pit of the stomach 
  to the top of the breast is 20 inches, and from the pit below 
  the breast bone to the top of the head 30 inches. 
  From the chin to the nostrils 40 inches..."
According to Leonardo, "From the chin to the roots of the hair is 1/10 of the whole figure". The manuscript says 
that this measurement equals 12 inches. In other words, 12 inches equals 1/10 of the whole figure. Therefore, the 
whole figure is 120 inches. All the other gaps can be filled in the same way.

For

text = "The whole figure is ... inches.
  From the chin to the roots of the hair is 12 inches.
  From the joint of the palm of the hand to the tip of 
  the longest finger is 13 inches. From the chin to
  the top of the head 15 inches; and from the pit of the stomach 
  to the top of the breast is ... inches, and from the pit below 
  the breast bone to the top of the head ... inches. 
  From the chin to the nostrils 40 inches..."
, the output should be

humanFigureProportions(text) = "Error"
According to Leonardo, "From the chin to the roots of the hair is 1/10 of the whole figure" and "From the joint of the 
palm of the hand to the tip of the longest finger is 1/10". Therefore, these two measurements should coincide. However, 
they have different values in the given text, so it cannot be restored according to da Vinci's proportions.

Please note that text in the examples has new lines only for the sake of readability. Actually, each testcase is a 
single string without newline characters.

Input/Output

[time limit] 4000ms (py)
[input] string text

A text following the format described above. It is guaranteed that there is at least one number in that text. It is also 
guaranteed that the numbers in the text don't exceed 1000.

[output] string

# Challenge's link: https://codefights.com/tournaments/395kwL88DqpgTwReK/B #
"""
def humanFigureProportions(text):
    proportions = [1, 10, 10, 8, 6, 4, 3]
    values = re.findall(r'\d+|\.\.\.', text)
    # drop the last one
    values.pop()
    
    ln = len(values)
    res = [0] * ln
    
    
    # find whole
    if values[0] != '...':
        whole = int(values[0])
    else:
        for i in range(ln):
            if values[i].isdigit():
                whole = int(values[i]) * proportions[i]
    
    
    # getting the values
    for i in range(ln):
        res[i] = whole * ( 1 / proportions[i])
    
    # check if values match with the results
    for i in range(ln):
        if values[i].isdigit():
            if int(values[i]) != res[i]:
                return "Error"
    
    index = 0
    words = text.split(" ")
    
    for i in range(len(words)):
        if words[i] == "...":
            words[i] = str(int(res[index]))
            index += 1
        elif words[i].isdigit():
            index += 1
    return " ".join(words)