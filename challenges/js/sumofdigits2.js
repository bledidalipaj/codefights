/*

 */

 function SumOfDigits2(n) {
    var sum = sumDigits(n);
    var nums = numAnswersBelow(sum.sum, sum.digits, sum.digits.length, true);
    return nums;
}

function sumDigits(n) {
    var answer = {sum: 0, digits: []};
    while(n > 0) {
        var digit = n % 10;
        answer.sum += digit;
        answer.digits.push(digit);
        n = Math.floor(n / 10);
    }
    return answer;
}

function numAnswersBelow(sum, digits, digitNum, considerDigits) {
    if(sum > digitNum * 9) return 0;
    if(sum < 0) return 0;
    if(sum === 0) return 1;    
    if(digitNum === 1) return 1;
    if(sum === digitNum * 9) return 1;
    
    var numPoss = 0;
    if(!considerDigits) {
        for(var i = 0; i < 10; ++i) {
            numPoss += numAnswersBelow(sum - i, digits, digitNum - 1, false);
        }
    } else {
        for(var i = 0; i < 10 && i < digits[digitNum-1]; ++i) {
            numPoss += numAnswersBelow(sum - i, digits, digitNum - 1, false);
        }
        numPoss += numAnswersBelow(sum - digits[digitNum-1], digits, digitNum - 1, true);
    }
    
    return numPoss;
}

/*
 * Next Solution
 */
 
var g_digits = [];
var g_lookup = [];
var g_base = 0;

function SumOfDigits2(n) {
    var digits = (""+n).split("");
    var result = 0;
    g_base = n;
    for (var i=0;i<digits.length;i++) {
        result+=parseInt(digits[i]);
        g_digits[i] = parseInt(digits[i]);
    }    
    return finalCount(digits.length,result);
}

function finalCount(n,sum) {
    console.log("count " + n + " digits for " + sum);
    for (var i=0; i<n; i++) {
        g_lookup[i] = [];
        for (var j=0; j<=sum; j++) {
            g_lookup[i][j] = -1;
        }
    }
    var ans = 0;
    for (var i=0; i<10; i++) {        
        if (i>sum) {
            break;
        }
        ans+=doCount(n-1,sum-i,""+i);
    }
    return ans;
}

function doCount(n,sum,number) {
    
    if (n == 0) {
        return (sum==0)?1:0;
    }
    
    if (g_lookup[n][sum] != -1 
        &&
       !(n+number.length==g_digits.length 
         && (""+g_base).startsWith(number))) {
		return g_lookup[n][sum];
    }

    var ans = 0;
    
    for (var i=0; i<10; i++) {
        if (sum-i >= 0) {
            if (parseInt(number+i+"00000000000".substr(0,n-1))>g_base) {
                break;
            }
            ans += doCount(n-1, sum-i, number+i);
        }
    }
    g_lookup[n][sum] = ans;

    return ans;
}