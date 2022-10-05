import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_14502_연구소 {
    static int N, M, answer = 0;
    static int[][] graph;
    static List<int[]> virus_list;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static Queue<int[]> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        virus_list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st.nextToken());
                graph[i][j] = num;
                if(num == 2) {
                    virus_list.add(new int[]{i, j});
                }
            }
        }

        make_wall(0);
        System.out.println(answer);

    }

    static void solution(int[][] map){
        queue = new LinkedList<>();

        for (int i = 0; i < virus_list.size(); i++) {
            queue.offer(virus_list.get(i));
        }

        while(!queue.isEmpty()){
            int[] point = queue.poll();
            int x = point[0];
            int y = point[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                if(map[nx][ny] == 1 || map[nx][ny] == 2) continue;
                map[nx][ny] = 2;
                queue.offer(new int[]{nx, ny});
            }
        }
        answer = Math.max(answer, cnt_zero(map));
    }

    static void make_wall(int depth){
        if(depth == 3){
            int[][] cp_graph = new int[N][M];

            for (int i = 0; i < N; i++) {
                System.arraycopy(graph[i], 0, cp_graph[i], 0, M);
            }
            solution(cp_graph);
            return;
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(graph[i][j] == 0) {
                    graph[i][j] = 1;
                    make_wall(depth + 1);
                    graph[i][j] = 0;
                }
            }
        }
    }

    static int cnt_zero(int[][] map){
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(map[i][j] == 0) cnt += 1;
            }
        }
        return cnt;
    }
}

// 벽을 3개 세우는 경우의 수를 모두 구하고
// 해당 경우의 수에서 완전 탐색 진행 후, 0의 개수가 최댓값인 경우의 해를 출력
