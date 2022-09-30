import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17070_파이프옮기기1 {
    static int N;
    static int[][] graph;
    static int[][][] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        graph = new int[N + 1][N + 1];
        dp = new int[N + 1][N + 1][3];

        dp[1][2][0] = 1;
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int x = 1; x <= N; x++) {
            for (int y = 3; y <= N; y++) {
                if (graph[x][y] == 1) continue;
                dp[x][y][0] = dp[x][y - 1][0] + dp[x][y - 1][2];
                dp[x][y][1] = dp[x - 1][y][1] + dp[x - 1][y][2];

                if (graph[x - 1][y] == 1 || graph[x][y - 1] == 1) continue;
                dp[x][y][2] = dp[x - 1][y - 1][0] + dp[x - 1][y - 1][1] + dp[x - 1][y - 1][2];
            }
        }
        int answer = 0;

        for (int i = 0; i < dp[N][N].length; i++) {
            answer += dp[N][N][i];
        }

        System.out.println(answer);
    }
}
