import java.util.*;

class Solution {
    boolean solution(String s) {
        char[] items = s.toCharArray();
        Stack<Character> stack = new Stack<>();
        
        for(char item: items) {
            if(item == '(') {
                stack.add(item);
                continue;
            }
            
            if(stack.isEmpty() || stack.peek() == ')') return false;
            stack.pop();
        }

        return stack.isEmpty();
    }
}