"""
A group of n people played a game in which the loser must double the money of the rest of the players. The game has been played n 
times, and each player has lost exactly once. Surprisingly, each player ended up with the same amount of money of m dollars.

Considering all that, find the amount of money each player had at the very beginning, and return it as an array of n elements sorted 
in descending order.

Example

For n = 3 and m = 16, the output should be
doubleTheMoneyGame(n, m) = [ 26.0, 14.0, 8.0 ].

Let's say that player A started with $26, player B had $14, and player C had $8.

After the first game, player A lost, and had to pay double the amount of players' B and C money. So the amount of money the players 
had at the end of the game was [ 4.0, 28.0, 16.0 ].

After the second game, player B lost, and the "money array" became [ 8.0, 8.0, 32.0 ].

After the third game, player C lost, the money became [ 16.0, 16.0, 16.0 ].

Input/Output

[time limit] 4000ms (py)
[input] integer n

The number of players, aka the number of played games.

Constraints:
2 ≤ n ≤ 7.

[input] integer m

The same amount of money each player has after n game played.

Constraints:
1 ≤ m ≤ 10000.

[output] array.float

The amount of money each player had in the beginning of the game sorted in descending order. It is guaranteed that the values in the output 
won't have more than 5 digits after the decimal point.

# https://codefights.com/challenge/4Mpg5NjZrFJtqvhGC/main #
"""
def doubleTheMoneyGame(n, m):
    res = [m * 1.0] * n
    
    for i in range(n):
        # loser = res[i]
        for j in range(n):
            if i != j:
                res[j] /= 2
                res[i] += res[j]
    return sorted(res, reverse=True)

def doubleTheMoneyGame(n, m):
    res = [m] * n
    for i in range(n):
        wasMoney = 0
        for j in range(n):
            if j == i:
                continue
            wasMoney += res[j] / 2.
            res[j] /= 2.
        res[i] += wasMoney
    return sorted(res, reverse=True)