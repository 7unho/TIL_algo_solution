import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1194_달이_차오른다 {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    static char[][] graph;
    static int[][] cnt;
    static int N, M;
    static List<Character> key_list;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int answer = 0;
        int start_x = 0;
        int start_y = 0;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new char[N][M];
        cnt = new int[N][M];
        key_list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            graph[i] = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                if(graph[i][j] == '0') {
                    Node node = new Node(i, j, 0, 0);
                } else if (graph[i][j] == '#'){
                    cnt[i][j] = -1;
                }
            }
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {start_x,  start_y});

        while(!queue.isEmpty()){
            int[] point = queue.poll();
            int x = point[0];
            int y = point[1];

            System.out.println("x : " + x + " y : " + y);

            if(graph[x][y] == '1') {
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                System.out.println("nx : " + nx +  " ny  : " + ny);

                if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                if(graph[nx][ny] == '#') continue;
                if(graph[nx][ny] >= 97 && graph[nx][ny] <= 122) key_list.add(graph[nx][ny]);
                if((graph[nx][ny] >= 65 && graph[nx][ny] <= 90) && !hasKey(nx, ny)) continue;
                cnt[nx][ny] = Math.min(cnt[nx][ny], cnt[x][y]) + 1;
                queue.offer(new int[]{nx, ny});
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(cnt[i]));
        }

    }

    public static boolean hasKey(int x, int y){
        boolean flag = false;
        for (int i = 0; i < key_list.size(); i++) {
            if((graph[x][y] + 32) == key_list.get(i)) flag = true;
        }
        return flag;
    }

    public static class Node{
        int x;
        int y;
        int cnt;
        int key;

        public Node(int x, int y, int cnt, int key) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.key = key;
        }

    }
}
//F
//
//AbF
//DeF

// bfs탐색을 진행하면서 대문자를 만나면 : key_list에 열쇠가 있는지 확인하고, 있다면 쭉 진행
//                                                             없다면 return
//                                1을 만나면 종료..