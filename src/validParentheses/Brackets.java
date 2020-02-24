package validParentheses;

import java.util.Stack;

public class Brackets {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            try {
                // Push opening brackets to Stack
                if (ch == '(' || ch == '{' || ch == '[') {
                    stack.push(ch);
                } else if (ch == ')' || ch == '}' || ch == ']') {
                    // Closing brackets in expression must match with Stack's top element
                    if (!isSameType(stack.pop(), ch)) {
                        return false;
                    }
                }
            } catch (Exception e) {
                // Element can't be popped since Stack is empty
                return false;
            }
        }
        return stack.isEmpty();
    }

    private static boolean isSameType(char ch1, char ch2) {
        return ch1 == '(' && ch2 == ')' ||
                ch1 == '{' && ch2 == '}' ||
                ch1 == '[' && ch2 == ']';
    }
}
