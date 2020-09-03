package uniquePaths;

class Unique {
    public int uniquePaths(int rows, int columns) {
        if (rows == 1 && columns == 1) {
            return 1;
        }
        int[][] dp = new int[rows][columns];
        helper(rows, columns, 0, 0, dp);
        return dp[0][0];
    }

    public boolean isValidSquare(int rows, int columns, int i, int j) {
        return i >= 0 && j >= 0 && i < rows && j < columns;
    }

    public int helper(int rows, int columns, int i, int j, int[][] dp) {
        if (!isValidSquare(rows, columns, i + 1, j) && !isValidSquare(rows, columns, i, j + 1)) {
            return 1;
        }
        if (dp[i][j] != 0) {
            return dp[i][j];
        }

        int sum = 0;
        if (isValidSquare(rows, columns, i + 1, j)) {
            sum += helper(rows, columns, i + 1, j, dp);
        }
        if (isValidSquare(rows, columns, i, j + 1)) {
            sum += helper(rows, columns, i, j + 1, dp);
        }
        dp[i][j] = sum;

        return sum;
    }

    public static void main(String[] args) {
        int m = 7, n = 3;
        System.out.println("Input: m = " + m + " n = " + n);
        System.out.println("Output: " + new Unique().uniquePaths(m, n));
    }
}