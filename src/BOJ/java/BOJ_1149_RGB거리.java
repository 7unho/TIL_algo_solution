import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_1149_RGB거리 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        int[][] graph = new int[N + 1][];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            graph[i] = new int[] {
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            };
        }

        for (int i = 2; i <= N; i++) {
            graph[i][0] += Math.min(graph[i - 1][1], graph[i - 1][2]);
            graph[i][1] += Math.min(graph[i - 1][0], graph[i - 1][2]);
            graph[i][2] += Math.min(graph[i - 1][1], graph[i - 1][0]);
        }

        Arrays.sort(graph[N]);
        System.out.println(graph[N][0]);

    }
}
