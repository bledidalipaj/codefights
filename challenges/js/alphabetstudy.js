/*
My little brother Jeff learns to read, and has already learnt a bunch of letters. Since boring letters memorizing 
isn't much fun, I would like to give him a book to read, which consists of various words. The thing is, I'm not 
sure if he will be able to read it.

I've extracted all the words from the book, and converted them to lowercase. Now I need your help: given the letters 
Jeff knows and a word, determine if Jeff will be able to read the word, i.e. if all the letters in the word are familiar to him.

Example

For letters = "act" and word = "cat", the output should be
AlphabetStudy(letters, word) ="Yes"`.

Jeff knows letters 'a', 'c' and 't', which is enough to read "cat".

For letters = "q" and word = "abc", the output should be
AlphabetStudy(letters, word) ="No"`.

Jeff knows only one letter, which is not enough to read the word.

Input/Output

[time limit] 4000ms (py)
[input] string word

A word consisting of lowercase English letters, all of which are guaranteed to be unique.

Constraints:
0 ≤ word.length ≤ 26.

[input] string word

A string of lowercase English letters.

Constraints:
1 ≤ word.length ≤ 20.

[output] string

"Yes" if Jeff will be able to read the word and "No" otherwise.

# Challenge's link: https://codefights.com/challenge/nA88LDtnefwn2TYrq #
 */
function AlphabetStudy(letters, word) {
    for (var i = 0; i < word.length; i++) {
        if (letters.indexOf(word[i]) == -1){
            return "No";
        }
    }
    return "Yes";
}
