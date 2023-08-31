import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(
            strings, 
            (v1, v2) -> {
                return ((v1.charAt(n) == v2.charAt(n))) ? v1.compareTo(v2) : v1.charAt(n) - v2.charAt(n);
            }
        );
        return strings;
    }
}