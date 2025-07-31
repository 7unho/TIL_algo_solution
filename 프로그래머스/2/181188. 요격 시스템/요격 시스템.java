import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        int boundary = 0;

        Arrays.sort(targets, Comparator.comparing(target -> target[1]));
        
        for (int[] target: targets) {
            if (target[0] < boundary) continue;
            answer += 1;
            boundary = target[1];
        }

        return answer;
    }
}