import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        Comparator<Integer> comparator = Comparator.comparingInt(Integer::intValue).reversed();
        Queue<Integer> q = new PriorityQueue<>(comparator);

        Arrays.stream(works).forEach(q::offer);

        for (int i = 0; i < n; i++) {
            int work = q.poll();
            q.offer(Math.max(work - 1, 0));
        }

        while (!q.isEmpty()) {
            int work = q.poll();
            answer += (work * work);
        }

        return answer;
    }
}