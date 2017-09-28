"""
Spring has sprung in the Northern Hemisphere!

As you walk through the park, you notice that the clover has started growing as well. You lean down and pick a clover 
that has a ridiculous number of leaves.

You believe that any clover that has a number of leaves divisible by 4 is lucky. Determine if the clover you found is 
lucky.

Example:

For leaves = "2075134854075614008885732002623615",
the output should be
crazyClover(leaves) = false.

For leaves = "32565527543186766526240463003010854254680",
the output should be
crazyClover(leaves) = true.

Input/Output

[time limit] 4000ms (py3)
[input] string leaves

The number of leaves on the clover you found.

Guaranteed constraints:
1 ≤ leaves.length ≤ 105.

[output] boolean

Return true if the clover you found is lucky, otherwise return false.

# Challenge's link: https://codefights.com/challenge/x8HkBKBW8PxKApXPs #
"""
crazyClover = lambda leaves: int(leaves) % 4 < 1