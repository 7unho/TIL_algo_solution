import java.util.*;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] spells = my_string.toCharArray();
        Set<Character> spellSet = new HashSet<>();
        
        for(char c: spells) {
            if(spellSet.contains(c)) continue;
            spellSet.add(c);
            answer += c;
        }
        
        return answer;
    }
}