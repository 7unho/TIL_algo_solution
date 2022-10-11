import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWE_4014_활주로건설 {
    static int N, X;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            int answer = 0;
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            X = Integer.parseInt(st.nextToken());

            int[][] graph = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0; i < N; i++) {
                answer += check(graph[i]);

                int[] temp = new int[N];
                for (int j = 0; j < N; j++) {
                    temp[j] = graph[j][i];
                }
                answer += check(temp);
            }

            System.out.printf("#%d %d\n", tc, answer);

        }
    }

    static int check(int[] temp){
        int cnt = 1;

        for (int i = 1; i < N; i++) {
            if(temp[i] == temp[i - 1]) cnt += 1;
            else if(temp[i] - 1 == temp[i - 1] && cnt >= X) cnt = 1;
            else if(temp[i] + 1 == temp[i - 1] && cnt >= 0) cnt = -X + 1;
            else return 0;
        }
        if(cnt >= 0) return 1;
        return 0;
    }
}
