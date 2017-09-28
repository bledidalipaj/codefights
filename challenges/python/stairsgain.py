"""
You're standing in front of a staircase with some steps painted gray and others painted yellow. When climbing up the stairs you can 
either put your foot on the next step, or on the one after it (i.e. you can step over the next step).

Putting your foot on a yellow step gives you 1 point and stepping over it gives you 2 points. When you put your your foot on a gray step 
you lose 2 points, and when you step over it you lose 1 point.

As the first move, you should put your foot to the first or the second step, and as your last move you must put your foot on the last step.

Determine the maximum possible score you can get having climbed up the stairs.

Example

For stairs = "ygy", the output should be
StairsGain(stairs) = 1.

According to the rules, there are three ways to go to the top of the stairs:

Stepping on each step. Then the score will be 1 + (- 2) + 1 = 0.
Stepping on the first step, stepping over the second step right at the third one. In this case the score is: 1 + (- 1) + 1 = 1.
Making the first move on the second step, and then moving on the third one. Here the score equals to: 2 + (- 2) + 1 = 1.
Thus, the highest possible score is 1.

Input/Output

[time limit] 4000ms (js)
[input] string stairs

A string consisting of letters "y" and "g" representing the sequence of colors of the stairs.

Constraints:
1 ≤ stairs.length ≤ 104.

[output] integer

The maximum possible score you can get having climbed up the stairs.
"""
def StairsGain(stairs):
    # No matter were you are standing, you should 
    # always pass the next step
    max_score = 0
    double = False
    for i in range(len(stairs)):
        if double:
            if stairs[i] == 'y':
                max_score += 2
            else:
                max_score -= 1
        else:
            if stairs[i] == 'y':
                max_score += 1
            else:
                max_score -= 2
        double = not double
    return max_score

def StairsGain(stairs):
    
    dp = [0, 0]
    stairs = 'd' + stairs # add dummy entry
    
    for i in range(1, len(stairs)):
        cur = stairs[i]
        prev = stairs[i - 1]
        
        price_from_prev = 1 if cur == 'y' else -2
        
        price_from_prev_prev = price_from_prev
        if prev == 'y':
            price_from_prev_prev += 2
        elif prev == 'g':
            price_from_prev_prev -= 1
            
        dp.append( max(dp[-1] + price_from_prev, 
                       dp[-2] + price_from_prev_prev) )
                  
    return dp[-1]