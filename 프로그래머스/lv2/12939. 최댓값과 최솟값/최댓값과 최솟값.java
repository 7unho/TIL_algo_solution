import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        int[] items = Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).toArray();
        int max = Arrays.stream(items).max().orElse(Integer.MAX_VALUE);
        int min = Arrays.stream(items).min().orElse(Integer.MIN_VALUE);
    
        return min + " " + max;
    }
}