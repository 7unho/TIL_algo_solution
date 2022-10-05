import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1600_말이되고픈원숭이 {
    // 원숭이 클래스 만들어서 k값 보내주기
    static int[][] graph;
    static int[][] cnt;
    static int[][] cpy_cnt;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int[] horse_dx = {1, 2, 2, 1, -1, -2, -2, -1};
    static int[] horse_dy = {-2, -1, 1, 2, 2, 1, -1, -2};
    static int K, N, M;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Queue<int[]> queue = new LinkedList<>();

        K = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        cnt = new int[N][M];
        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            Arrays.fill(cnt[i], -1);
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

            }
        }

        queue.offer(new int[]{0, 0});
        cnt[0][0] = 0;

        while(!queue.isEmpty()){
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                if(graph[nx][ny] == 1) continue;
                if(cnt[nx][ny] == -1){
                    cnt[nx][ny] = cnt[x][y] + 1;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }

        for (int j = 0; j < N; j++) {
            System.out.println(Arrays.toString(cnt[j]));
        }

        for (int i = 0; i < K; i++) {
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < M; y++) {
                    if(graph[x][y] == 1) continue;
                    cpy_cnt = cnt;
                    answer = Math.min(hosre_bfs(x, y), answer);
                    for (int j = 0; j < N; j++) {
                        System.out.println(Arrays.toString(cpy_cnt[j]));
                    }
                }
            }

        }

        System.out.println(answer);


    }

    public static int hosre_bfs(int x, int y){
        System.out.println("x -> " + x + "y -> " + y);
        for (int i = 0; i < 8; i++) {

            int nx = x + horse_dx[i];
            int ny = y + horse_dy[i];
            System.out.println("nx -> " + nx + "ny -> " + ny);

            if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
            if(graph[nx][ny] == 1) continue;
            cpy_cnt[nx][ny] = Math.min(cpy_cnt[x][y] + 1, cnt[nx][ny]);
        }

        return cpy_cnt[N - 1][M - 1];
    }
}


// bfs로 탐색한다.
// 탐색 조건 : 0 <= nx, ny < N,