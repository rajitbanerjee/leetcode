/**
 * https://leetcode.com/problems/reverse-integer/ : Given a 32-bit signed integer,
 * reverse digits of an integer. Assume we are dealing with an environment which
 * could only store integers within the 32-bit signed integer range: [−2^31,
 * 2^31 − 1]. For the purpose of this problem, assume that your function returns
 * 0 when the reversed integer overflows.
 */
public class RevInt {
    public int reverse(int x) {
        long copy = x, rev = 0;

        // reverse the number digit-by-digit
        while (copy != 0) {
            rev = rev * 10 + copy % 10;
            copy = copy / 10;
        }

        // overflow case
        if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE)
            return 0;
        else
            return (int) (rev); // convert long to int and return

    }
}