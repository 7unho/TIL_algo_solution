import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

// 기본 Knapsack 문제,
// 배낭에 넣을 수 있는 물건들의 가치합의 최댓갑 !
public class BOJ_12865_평범한배낭 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[][] dp = new int[N + 1][K + 1];
        List<Thing> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            list.add(new Thing(w, v));
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                int w = list.get(i - 1).w;
                int v = list.get(i - 1).v;

                if(j < w){
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - w] + v);
                }
            }
        }

        System.out.println(dp[N][K]);
    }

}

class Thing{
    int w;
    int v;

    public Thing(int w, int v) {
        this.w = w;
        this.v = v;
    }
}
