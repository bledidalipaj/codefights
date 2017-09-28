/*
Only Survivor

Some guys holding swords are playing a game. This game will be the last one for most of them.

The rules of the game are the following: the players are standing in a circle. Person number 1 starts the game by killing the 
guy to the left of him. After that, the next living person to his left kills his the closest person to their left of him who is 
still alive. The game continues until there's only one person left.

Your task is, given the number of players playing the game, to find the last survivor and return the one-based position of that 
person. Assume that the person who starts the game has number 1, and the players are enumerated in the clockwise direction.

Example

For n = 10, the output should be
onlySurviver(n) = 5.

Here's why:

	
Person 1 kills Person 2
Person 3 kills Person 4
Person 5 kills Person 6
Person 7 kills Person 8
Person 9 kills Person 10
Person 1 kills Person 3
Person 5 kills Person 7
Person 9 kills Person 1
Person 5 kills Person 9
The output should be: 5.
Input/Output

[time limit] 4000ms (js)
[input] integer players

Constraints:
0 < players < 231.

[output] integer

1-based position of the survivor of the game.

# Challenge's link: https://codefights.com/challenge/gmYZRfrxWt6Ka7gYo #
*/
function onlySurviver(players) {
    return (players - Math.pow(2, parseInt(Math.log2(players)))) * 2 + 1;

}

/*
 * onlySurviver(1) = 1
 * onlySurviver(2) = 1
 * onlySurviver(3) = 3
 * onlySurviver(4) = 1
 * onlySurviver(5) = 3
 * onlySurviver(6) = 5
 * onlySurviver(7) = 7
 * onlySurviver(8) = 1
 */