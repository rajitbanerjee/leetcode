package implementStrStr;

import java.util.ArrayList;

public class Implement {
    public int strStr(String haystack, String needle) {
        if (needle.trim().equals("")) {
            return 0;
        } else {
            ArrayList<Integer> indices = new ArrayList<>();
            char ch = needle.charAt(0);
            // add all the indices in haystack which are equal to the start of needle
            for (int i = 0; i <= haystack.length() - needle.length(); i++) {
                if (haystack.charAt(i) == ch) {
                    indices.add(i);
                }
            }
            // if no index in haystack starts with needle's first char, return -1
            if (indices.isEmpty()) {
                return -1;
            }
            // check if the entire needle is present at the previously found indices
            for (int i : indices) {
                if (haystack.substring(i).startsWith(needle)) {
                    return i;
                }
            }
            return -1;
        }
    }
}
