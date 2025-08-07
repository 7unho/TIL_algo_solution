import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long[] requests = new long[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            requests[i] = Long.parseLong(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        long M = Long.parseLong(st.nextToken());

        if (Arrays.stream(requests).sum() <= M) {
            System.out.println(Arrays.stream(requests).max().getAsLong());
            System.exit(0);
        }
        
        long start = 1;
        long end = 10_000_000_001L;
        long answer = 0;

        while (start <= end) {
            long mid = (start + end) / 2;
            if (getTotalBudget(mid, requests) <= M) {
                answer = Math.max(answer, mid);
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        System.out.println(answer);
    }

    private static long getTotalBudget(long mid, long[] requests) {
        long answer = 0;
        for (long request: requests) {
            answer += Math.min(mid, request);
        }
        return answer;
    }


}