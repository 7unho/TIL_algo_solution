import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());
        int M = Integer.parseInt(tokenizer.nextToken());
        int[] playTimes = new int[N];

        tokenizer = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            playTimes[i] = Integer.parseInt(tokenizer.nextToken());
        }

        long start = Arrays.stream(playTimes).max().getAsInt();
        long end = 10_000_000_000L; // 최대 강의 시간 * N
        long answer = 10_000_000_000L;
        
        while (start <= end) {
            long mid = (start + end) / 2;
            int cnt = getCount(playTimes, mid);
            
            if (cnt <= M) {
                end = mid - 1;
                answer = Math.min(answer, mid);
            } else {
                start = mid + 1;
            }
        }

        System.out.println(answer);
    }

    private static int getCount(int[] playTimes, long window) {
        int cnt = 1;
        int sum = 0;
        for (int i = 0; i < playTimes.length; i++) {
            if (sum + playTimes[i] > window) {
                cnt += 1;
                sum = playTimes[i];
            } else {
                sum += playTimes[i];
            }
        }
        return cnt;
    }
}