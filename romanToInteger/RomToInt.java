/**
 * https://leetcode.com/problems/roman-to-integer/ : Given a roman numeral, 
 * convert it to an integer. Input is guaranteed to be within the range from 
 * 1 to 3999.
 */
public class RomToInt {
    public int romanToInt(String rom) {
        int i, len = rom.length(), dec = 0;
        for (i = 0; i < len - 1; i++) {
            char ch = rom.charAt(i);
            char ch2 = rom.charAt(i + 1);
            if (convert(ch) < convert(ch2))
                dec -= convert(ch);
            else
                dec += convert(ch);
        }
        dec += convert(rom.charAt(len - 1));
        return dec;
    }

    int convert(char x) {
        switch (x) {
        case 'M': return 1000;
        case 'D': return 500;
        case 'C': return 100;
        case 'L': return 50;
        case 'X': return 10;
        case 'V': return 5;
        case 'I': return 1;
        default:  return 0;
        }
    }
}
