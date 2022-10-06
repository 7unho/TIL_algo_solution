import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SWE_3307_증가부분수열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            int N = Integer.parseInt(br.readLine());

            int[] graph = new int[N];
            int[] dp = new int[N];
            int answer = 0;
            Arrays.fill(dp, 1);

            st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                graph[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < i; j++) {
                    if(graph[i] >= graph[j]) dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }

            for (int i = 0; i < N; i++) {
                answer = Math.max(answer, dp[i]);
            }

            System.out.printf("#%d %d\n", tc, answer);
        }
    }
}
