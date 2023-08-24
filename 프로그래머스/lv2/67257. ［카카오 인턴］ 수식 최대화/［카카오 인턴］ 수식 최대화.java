import java.util.*;

class Solution {
    static String[][] priority = {
        {"*", "-", "+"},
        {"*", "+", "-"},
        {"+", "-", "*"},
        {"+", "*", "-"},
        {"-", "+", "*"},
        {"-", "*", "+"}
    };
    
    public long solution(String expression) {
        StringTokenizer st = new StringTokenizer(expression, "*+-", true);
        List<String> tokens = new ArrayList<>();
        
        while(st.hasMoreTokens()) tokens.add(st.nextToken());
        
        long max = Long.MIN_VALUE;
        
        for(String[] opList: priority){
            long CASE = Math.abs(calculator(new ArrayList<>(tokens), opList));
            
            if(max < CASE) max = CASE;
        }
        return max;
    }
    
    public long calculator(long lNum, long rNum, String op){
        return switch(op){
                case "*" -> lNum * rNum;
                case "+" -> lNum + rNum;
                case "-" -> lNum - rNum;
                default -> 0;
        };
    }
    
    public long calculator(List<String> tokens, String[] opList){
        for(String op: opList){
            for(int i = 0; i < tokens.size(); i++){
                if(!op.equals(tokens.get(i))) continue;
                
                long lNum = Long.parseLong(tokens.get(i - 1));
                long rNum = Long.parseLong(tokens.get(i + 1));
                long sum = calculator(lNum, rNum, op);
                
                tokens.remove(i - 1);
                tokens.remove(i - 1);
                tokens.remove(i - 1);
                tokens.add(i - 1, String.valueOf(sum));
                
                i -= 2;
            }
        }
        
        return Long.parseLong(tokens.get(0));
    }
}