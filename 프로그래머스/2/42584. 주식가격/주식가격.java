import java.util.*;

class Solution {
    static int N;
    static int[] answer;
    static Stack<int[]> stack;
    public int[] solution(int[] prices) {
        N = prices.length;
        answer = new int[N];
        stack = new Stack<>();
        
        for(int i = 0; i < N; i++) process(stack, prices[i], i);
        setAnswers(stack);
        return answer;
    }
    
    public void process(Stack<int[]> stack, int price, int time) {
        while(!stack.isEmpty() && stack.peek()[0] > price) {
            int[] item = stack.pop();
            
            answer[item[1]] = time - item[1];
        }
        stack.push(new int[]{price, time});
    }
    
    public void setAnswers(Stack<int[]> stack) {
        while(!stack.isEmpty()) {
            int[] item = stack.pop();
            
            answer[item[1]] = N - 1 - item[1];
        }
    }
}