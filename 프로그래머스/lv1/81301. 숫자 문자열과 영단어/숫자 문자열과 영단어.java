import java.util.*;

class Solution {
    public int solution(String s) {
        String[] keys = new String[] {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        
        for(int key = 0; key < 10; key ++){
            s = s.replace(keys[key], Integer.toString(key));
        }
    
        return Integer.valueOf(s);
    }
}