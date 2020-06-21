package longestCommonPrefix;

/**
 * https://leetcode.com/problems/longest-common-prefix/ : Write a function to
 * find the longest common prefix string amongst an array of strings. If there
 * is no common prefix, return an empty string "".
 */
public class Prefix {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";
        String minStr = strs[0];
        String prefix = ""; // initialise prefix

        // find the smallest string
        for (String str : strs) {
            if (str.length() < minStr.length())
                minStr = str;
        }

        char[] letters = new char[strs.length];
        for (int i = 0; i < minStr.length(); i++) {
            for (int j = 0; j < strs.length; j++) {
                letters[j] = strs[j].charAt(i);
            }
            char min = letters[0], max = letters[0];
            for (char letter : letters) {
                if (letter < min)
                    min = letter;
                if (letter > max)
                    max = letter;
            }
            // if all the letters at some index are same, then form prefix
            if (min == max)
                prefix += min;
            else
                return prefix;
        }
        return prefix;
    }
}