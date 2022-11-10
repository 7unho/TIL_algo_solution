import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWE_7733_치즈도둑 {
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int answer, N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= TC; tc++) {
            N = Integer.parseInt(br.readLine());
            // 0일 일 때, 덩어리 개수는 1개이므로.
            answer = 1;

            graph = new int[N][N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            for (int day = 1; day <= 100; day++) {
                updateGraph(day);
                visited = new boolean[N][N];
                int cnt = 0;

                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if(dfs(i, j)) cnt += 1;
                    }
                }
                answer = Math.max(answer, cnt);
            }
            System.out.printf("#%d %d\n", tc, answer);

        }
    }

    static void updateGraph(int day) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] <= day) graph[i][j] = -1;
            }
        }
    }

    static boolean dfs(int x, int y) {
        if (x < 0 || y < 0 || x >= N || y >= N) return false;

        if (graph[x][y] > 0 && !visited[x][y]) {
            visited[x][y] = true;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                dfs(nx, ny);
            }
            return true;
        }
        return false;
    }
}
