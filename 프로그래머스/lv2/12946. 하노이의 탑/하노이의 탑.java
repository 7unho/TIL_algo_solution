import java.util.*;
// N개의 원반을 현재(current) 기둥에서 목표 기둥(next)로 옮기는 문제
// (n, currrent, next)
class Solution {
    public List<int[]> solution(int n) {
        return hanoi(n, 1, 3);
    }
    
    public List<int[]> hanoi(int n, int current, int next){
        // 1. 종료조건
        if(n == 1) return List.of(new int[] {current, next});
        
        int empty = 6 - (current + next);
        
        // (n, current, next) = (n - 1, current, empty) + (1, current, next) + (n - 1, empty, next)
        List<int[]> answer = new ArrayList<int[]>();
        answer.addAll(hanoi(n - 1, current, empty));
        answer.addAll(hanoi(1, current, next));
        answer.addAll(hanoi(n - 1, empty, next));
        
        return answer;  
    }
}