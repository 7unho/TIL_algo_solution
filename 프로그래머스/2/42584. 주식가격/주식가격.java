import java.util.*;

class Solution {
    static int[] answer;
    public int[] solution(int[] prices) {
        int N = prices.length;
        answer = new int[N];
        Stack<int[]> stack = new Stack<>();
        
        for(int i = 0; i < N; i++) {
            process(stack, prices[i], i);
            stack.push(new int[]{prices[i], i});
        }
        
        while(!stack.isEmpty()) {
            int[] item = stack.pop();
            
            answer[item[1]] = N - 1 - item[1];
        }
        return answer;
    }
    
    public void process(Stack<int[]> stack, int price, int time) {
        if(stack.isEmpty() || stack.peek()[0] <= price) return;
        
        while(!stack.isEmpty() && stack.peek()[0] > price) {
            int[] item = stack.pop();
            
            answer[item[1]] = time - item[1];
        }
    }
}