import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        rocks = Arrays.copyOf(rocks, rocks.length + 1);
        rocks[rocks.length - 1] = distance;
        Arrays.sort(rocks);
        
        int start = 1;
        int end = distance + 1;
        
        while((end - start) > 1) {
            int mid = (start + end) / 2;
            
            if(isValid(mid, rocks, n)) start = mid;
            else end = mid;
        }
        
        
        return start;
    }
    
    static boolean isValid(int d, int[] rocks, int n) {
        int removed = 0;
        int last = 0;
        
        for(int rock: rocks) {
            if(rock - last < d) {
                removed += 1;
                continue;
            }
            
            last = rock;
        }
        
        return removed <= n;
    }
}