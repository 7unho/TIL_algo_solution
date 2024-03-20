import java.util.*;
import java.util.stream.*;
class Solution {
    static int S;
    public int solution(String s) {
        int answer = 0;
        char[] param = s.toCharArray();
        S = param.length;
        for(int space = 0; space < S; space++) {
            if(!isValid(converter(param, space))) continue;
            answer += 1;
        }
        return answer;
    }
    
    
    // 괄호 회전 함수
    public char[] converter(char[] arr, int space) {
        char[] res = new char[S];
        for(int i = 0; i < S; i++) res[(S + i - space) % S] = arr[i];
        return res;
    }
    
    public boolean isValid(char[] items) {
        Stack<Character> stack = new Stack<>();
        for(char item: items) {
            switch(item) {
                case ')':
                    if(stack.isEmpty() || stack.peek() != '(') return false;
                    stack.pop();
                    break;
                case '}':
                    if(stack.isEmpty() || stack.peek() != '{') return false;
                    stack.pop();
                    break;
                case ']':
                    if(stack.isEmpty() || stack.peek() != '[') return false;
                    stack.pop();
                    break;
                    
                // 여는 괄호일 경우, push
                default:
                    stack.add(item);
                    break;
            }
        }
        return stack.isEmpty();
    }
}