import java.util.*;

// N개의 원반을 현재 기둥에서 목표 기둥으로 옮기는 문제
// (n, current, target)
class Solution {
    public List<int[]> solution(int n) {
        List<int[]> answer = new ArrayList<int[]>();
        hanoi(n, 1, 3, answer);
        return answer;
    }
    
    public void hanoi(int n, int current, int target, List<int[]> answer){
        if(n == 1){
            answer.add(new int[] {current, target});
            return;
        }
        
        // empty = 빈 기둥
        int empty = 6 - (current + target);
        
        // (n, current, target) = (n - 1, current, empty) + (1, current, target) + (n - 1, empty, target)
        hanoi(n - 1, current, empty, answer);
        hanoi(1, current, target, answer);
        hanoi(n - 1, empty, target, answer);
    }
}