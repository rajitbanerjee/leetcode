package nthTribonacciNumber;

public class Tribonacci {
    // Iterative is faster than recursive solution due to memory constraints
    public int tribonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1 || n == 2) {
            return 1;
        } else {
            int a = 0, b = 1, c = 1, d = 0;
            for (int i = 0; i < n - 2; i++) {
                d = a + b + c;
                a = b;
                b = c;
                c = d;
            }
            return d;
        }
    }
}
