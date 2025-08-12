import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        if (s < n) return new int[]{-1};
        
        int[] answer = new int[n];
        int base = s / n;
        int mod = s % n;

        Arrays.fill(answer, base);

        for (int i = 0; i < mod; i++) {
            answer[n - 1 - i] += 1;
        }

        return answer;
    }
}