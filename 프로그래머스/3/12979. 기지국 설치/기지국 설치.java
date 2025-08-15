/**
n := 아파트 개수
stations := 현재 기지국이 설치된 아파트 번호 ( 1 ~ N )
W := 전파 도달 거리

answer := 모든 아파트가 커버되는 기지국의 최소 개수
*/

import java.util.*;

class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int range = 2 * w + 1;
        int start = 0;
        
        for (int station: stations) {
            int left = Math.max(0, station - w - 1);
            int right = Math.min(n - 1, station + w - 1);
            
            if (start < left) {
                int gap = left - start;
                answer += (gap + range - 1) / range;
            }
            
            start = Math.max(start, right + 1);
            if (start >= n) break;
        }
        
        if (start < n) {
            int gap = n - start;
            answer += (gap + range - 1) / range;
        }
            
        return answer;
    }
}