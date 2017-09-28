"""
Imagine that you used time machine to travel to some ancient Kingdom. Unfortunately you got lost, and 
there are no maps to help you. Luckily you stumbled upon a fancy town, and now while you're waiting for 
the "time-ship" to get back and rescue you, you have to find a job in the town to earn your living. There 
is no developer position available in the town, so you decided to work as a cashier in a souvenir shop.

You enjoy working in the shop except for one thing: giving exchange.
Here is the problem: the monetary system is not yet well designed, so the coins the folks use have arbitrary 
values (unlike in the modern world, where the values of money are only the product of 1, 2 an 5). The shop 
owner wants you to always deliver "the best customer service", so you have to give exchange to customers with 
the smallest possible number of coins for their convenience. Moreover, in case there are several ways to do 
this, you should give change that will have the greatest number of high-value coins in it.

The shop’s owner gives you practically unlimited number of coins of each value. You decide to make the first 
software ever in the Kingdom and write a program that given the coins values and the change will give a combination 
of coins that should be given in exchange.

Example

For coins = [2, 3, 4] and change = 6, the output should be
bestCoinsExchange(coins, change) = [[4, 1], [2, 1]].

There are several ways to give change:

2, 2, 2;
3, 3;
4, 2.
The first option shouldn't be considered, since it consists of 3 coins, unlike other options that consist of only 
2 coins each.
The third option should be chosen instead of the second one since it contains a coin of value 4, and the largest 
value of a coin in the second option is only 3.

Input/Output

[time limit] 4000ms (py3)
[input] array.integer coins

Array of distinct coins, sorted in ascending order.

Constraints:
1 ≤ coins.length ≤ 1000,
1 ≤ coins[i] ≤ 1000.

[input] integer change

The change you need to give back to a customer.

Constraints:
1 ≤ change ≤ 5000.

[output] array.array.integer

The output should contain the coins that should be given to the customer. Each coin should be given in the format
 [<coin_value>, <number_of_coins>].
The output should be sorted by <coin_value>s in descending order.

It is guaranteed that it's always possible to give the change.

# Challenge's link: https://codefights.com/challenge/vFup7mXP4Sdfpx6TY/solutions/4ntB4LyPaRjc5RbHe #
"""
def bestCoinsExchange(coins, change):
    change += 1
    dp = [float('inf')] * change
    last = [-1] * change
    dp[0] = 0
    for i in range(1, change):
        for j, coin in enumerate(coins):
            if coin > i:
                break
            if dp[i - coin] + 1 <= dp[i]:
                dp[i] = dp[i - coin] + 1
                last[i] = j

    used_coins = [0] * len(coins)
    cur = change - 1
    while cur != 0:
        used_coins[last[cur]] += 1
        cur -= coins[last[cur]]
        
    res = [[coins[i], cnt] for i, cnt in enumerate(used_coins) if cnt > 0][::-1]
    return res