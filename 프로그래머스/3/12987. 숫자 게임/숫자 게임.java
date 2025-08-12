import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        int N = A.length;
        List<Integer> aList = Arrays.stream(A).boxed().sorted(Collections.reverseOrder()).collect(Collectors.toList());
        Deque<Integer> bQ = new LinkedList<>();
        Arrays.stream(B).boxed().sorted(Collections.reverseOrder()).forEach(bQ::offer);

        for (int i = 0; i < N; i++) {
            int a = aList.get(i);
            int b = bQ.poll();
            if (b > a) {
                answer += 1;
            } else {
                bQ.addFirst(b);
                bQ.removeLast();
            }
        }
        
        return answer;
    }
}