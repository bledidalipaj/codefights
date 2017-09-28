"""
Misha and Vanya have played several sets of table tennis. Each set consists of several serves. Each serve 
is won by one of the players, who receives one point while the loser receives no points. Once one of the 
players scores exactly k points, the scoreboard is reset and a new set begins.

Across all the sets, Misha scored a total of a points and Vanya scored b points. Given this information, 
determine the maximum number of sets they could have played.

Note: The rules of the game in this problem differ from real table tennis rules. For example, the rule of 
"balance", which says that the winning player has to be at least two points ahead to win a set, doesn't apply 
to this problem.

Example
For k = 11, a = 11 and b = 5, the output should be
tableTennisGame(k, a, b) = 1.

They have completed a maximum of one game, because a, the number of points Misha scored, is equal to k.

Input/Output

[time limit] 4000ms (py)
[input] integer k

An integer representing the number of points one player must score before the scoreboard is reset and a new set 
begins.

Constraints:
1 ≤ k ≤ 109

[input] integer a

An integer representing the number of points Misha scored across all the sets.

Constraints:
1 ≤ a ≤ 109

[input] integer b

An integer representing the number of points Vanya scored across all the sets.

Constraints:
1 ≤ b ≤ 109

[output] integer

An integer representing the maximum number of sets Misha and Vanya could have played.
"""
def tableTennisGame(k, a, b):
    return a / k + b / k