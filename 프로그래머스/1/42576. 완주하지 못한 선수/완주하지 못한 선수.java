import java.util.*;

class Solution {
    public Map<String, Integer> mapBuilder(String[] members) {
        Map<String, Integer> map = new HashMap<>();
        
        for (String m : members) {
            map.putIfAbsent(m, 0);
            map.put(m, map.get(m) + 1);
        }
        
        return map;
    }
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = mapBuilder(participant);
        
        for (String c: completion) {
            int v = map.get(c) - 1;
            if(v == 0) {
                map.remove(c);
                continue;
            }
            map.put(c, v);
            
        }
        
        return map.keySet().iterator().next();
    }
}