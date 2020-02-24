package validParentheses;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BracketsTest {
    @Test
    void testBrackets() {
        Brackets b = new Brackets();
        assertTrue(b.isValid("()"));
        assertTrue(b.isValid("()[]{}"));
        assertTrue(b.isValid("{[]}"));
        assertFalse(b.isValid("(})"));
        assertFalse(b.isValid("([)]"));
    }
}