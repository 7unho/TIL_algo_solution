import java.util.*;
class Solution {
    static String[][] priority = {
        {"*", "-", "+"},
        {"*", "+", "-"},
        {"+", "*", "-"},
        {"+", "-", "*"},
        {"-", "*", "+"},
        {"-", "+", "*"}
    };
    
    public long calculator(long a, long b, String op){
        return switch(op){
            case "*" -> a * b;
            case "+" -> a + b;
            case "-" -> a - b;
            default -> 0;
        };
    }
    
    public long calculator(List<String> tokens, String[] priority){
        for(String op: priority){
            for(int i = 0; i < tokens.size(); i++){
                if(!op.equals(tokens.get(i))) continue;
                
                long a = Long.parseLong(tokens.get(i - 1));
                long b = Long.parseLong(tokens.get(i + 1));
                
                long res = calculator(a, b, op);
                
                tokens.remove(i - 1);
                tokens.remove(i - 1);
                tokens.remove(i - 1);
                tokens.add(i - 1, String.valueOf(res));
                i -= 2;
            }
        }
        
        return Math.abs(Long.parseLong(tokens.get(0)));
    }
    public long solution(String expression) {
        StringTokenizer st = new StringTokenizer(expression, "*-+", true);
        List<String> tokens = new ArrayList<>();
        while(st.hasMoreTokens()){
            tokens.add(st.nextToken());
        }
        
        long max = 0;
        for(String[] p: priority){
            long value = calculator(new ArrayList<>(tokens), p);
            if(max < value) max = value;
        }
        
        return max;
    }
}