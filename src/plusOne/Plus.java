package plusOne;

public class Plus {
    public int[] plusOne(int[] digits) {
        boolean isAllNine = true;
        for (int digit : digits) {
            if (digit != 9) {
                isAllNine = false;
                break;
            }
        }
        if (isAllNine) {
            // if the array contains N * 9's, the answer is 1 and N * 0's
            int[] ans = new int[digits.length + 1];
            ans[0] = 1;
            return ans;
        } else {
            // ripple carry 1 adder
            digits[digits.length - 1] += 1;
            for (int i = digits.length - 1; i >= 1; i--) {
                if (digits[i] == 10) {
                    digits[i] = 0;
                    digits[i - 1] += 1;
                }
            }
            return digits;
        }
    }
}
