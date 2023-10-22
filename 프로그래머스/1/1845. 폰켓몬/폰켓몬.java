import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = nums.length / 2;
        Set<Integer> items = new HashSet<>();
        
        for(int n: nums) items.add(n);
        
        return (answer <= items.size())? answer: items.size();
    }
}