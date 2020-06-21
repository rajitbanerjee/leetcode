package palindromeInteger;

/**
 * https://leetcode.com/problems/palindrome-number/ : Determine whether an integer
 * is a palindrome. An integer is a palindrome when it reads the same backward
 * as forward.
 * Follow up: Could you solve it without converting the integer to a string?
 */
public class Palin {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false; // negatives can't be palindromes
        else {
            int copy = x, rev = 0;
            while (copy != 0) {
                rev = rev * 10 + copy % 10; // reversing the integer
                copy /= 10;
            }
            return (rev == x);
        }

    }
}