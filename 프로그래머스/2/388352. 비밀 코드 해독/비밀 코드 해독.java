/**
N := 1 ~ N 의 정수 범위, 10 ~ 30
q := 시도한 배열 목록
ans := q와 정답의 일치 개수
*/
import java.util.*;
import java.util.stream.*;

class Solution {
    static List<Set<Integer>> candidates;
    static int N;
    public int solution(int n, int[][] q, int[] ans) {
        N = n;
        candidates = new ArrayList<>();
        buildCandidates(0, new LinkedHashSet<>());
        
        candidates.removeIf(candidate -> {
            for (int i = 0; i < q.length; i++) {                
                if (!isMatched(q[i], ans[i], candidate)) {
                    return true;
                }
            }
            return false;
        });
        
        return candidates.size();
    }
    
    boolean isMatched(int[] q, int count, Set<Integer> candidate) {
        return Arrays.stream(q)
            .filter(candidate::contains)
            .count() == count;
    }
    
    static void buildCandidates(int start, Set<Integer> candidate) {
        if (candidate.size() == 5) {
            candidates.add(new LinkedHashSet<>(candidate));
            return;
        }
        
        for (int i = start + 1; i <= N; i++) {
            candidate.add(i);
            buildCandidates(i, candidate);
            candidate.remove(i);
        }
    }
}