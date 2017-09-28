/*
Recently Lucky learnt how to check if the given number is prime or not. Bunny, Lucky's friend, decided to give her a task to test her skills.

Let's call number P Prime Prime if the number of prime numbers in the range [1, P] is prime. Bunny asked Lucky to calculate the number of Prime 
Prime numbers in the range [l, r]. Can you you help her?

Example

For l = 1 and r = 10, the output should be
luckyandprimeprime(l, r) = 4.

There're 4 prime numbers in the given range: 2, 3, 5 and 7. Thus, Prime Prime numbers are 3, 4, 5 and 6, 4 numbers altogether.

Input/Output

[time limit] 4000ms (js)
[input] integer l

Constraints:
1 ≤ l ≤ r.

[input] integer r

Constraints:
l ≤ r ≤ 105.

[output] integer

The number of Prime Prime numbers in the range [l, r].

# Challenge's link: https://codefights.com/challenge/doXskkj8PMAJ27Epk/main #
*/

function luckyandprimeprime(l, r) {
    function isPrime(num){
        if(num < 2){
            return false;
        }
        
        var i = 2;
        while(i * i <= num){
            if(num % i == 0){
                return false;
            }
            i += 1
        }
        
        return true;
    }
    
    var primes = [];
    var length = 0;
    var ans = 0;
    
    for(var i = 2; i <= r; i++){
        if(isPrime(i)){
            primes.push(i);
            length += 1;
        }
        
        if(primes.indexOf(length) != -1 && i >= l){
            ans += 1;
            
        }
    }
    
    return ans;
}
