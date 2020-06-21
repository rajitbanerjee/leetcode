package lengthOfLastWord;

public class Word {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int index = s.lastIndexOf(' ');
        if (index == -1) {
            return s.length();
        } else {
            return s.substring(index + 1).length();
        }

    }
}
