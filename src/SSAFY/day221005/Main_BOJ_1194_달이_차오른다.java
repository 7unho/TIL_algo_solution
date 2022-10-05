import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main_BOJ_1194_달이_차오른다 {
    static char[][] graph;
    //[N][M][Key]
    // key ['a'] -> 000001
    // key'['f'] -> 100000
    // key['a','b','c','d','e','f'] -> 111111
    static boolean[][][] visited;
    static Node start;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int N, M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new char[N][M];
        visited = new boolean[N][M][64];

        for (int i = 0; i < N; i++) {
            graph[i] = br.readLine().toCharArray();

            for (int j = 0; j < M; j++) {
                if (graph[i][j] == '0') {
                    start = new Node(i, j, 0, 0);
                }
            }
        }

        bfs(start.x, start.y);
    }

    static void bfs(int x, int y) {
        Queue<Node> q = new LinkedList<>();

        q.add(new Node(x, y, 0, 0));
        visited[x][y][0] = true;

        // 종료조건
        // 1. 갈 수 있는 모든 경로를 탐색했다면
        while (!q.isEmpty()) {
            Node temp = q.poll();
            int count = temp.count;
            int key = temp.key;

            // 종료조건
            // 2. 탈출로에 도착했다면
            if (graph[temp.x][temp.y] == '1') {
                System.out.println(count);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = temp.x + dx[i];
                int ny = temp.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

                if (graph[nx][ny] == '#' || visited[nx][ny][key]) continue;

                // graph[nx][ny]가 열쇠일 때 -> 'a' ~ 'f'
                if (graph[nx][ny] - 'a' >= 0 && graph[nx][ny] - 'a' < 6) {

                    // 현재 가지고 있는 키가 'a'이고, 현재 지점에서 얻은 키가 'b'일 때.
                    // key : 000001;
                    // graph[nx][ny] - 'a' -> 1
                    // nKey = 000010 = 000011 따라서, nKey 는 'a'와 'b'를 가지고 있다를 뜻하게 된다.
                    //          or
                    //        000001
                    int nKey = (1 << (graph[nx][ny] - 'a')) | key;

                    // 해당 좌표에 nKey값을 가지고 방문한 적이 없다면
                    if (!visited[nx][ny][nKey]) {
                        visited[nx][ny][nKey] = true;
                        visited[nx][ny][key] = true;
                        q.add(new Node(nx, ny, count + 1, nKey));
                    }
                }

                // graph[nx][ny]가 문일 때 -> 'A' ~ 'F'
                else if (graph[nx][ny] - 'A' >= 0 && graph[nx][ny] - 'A' < 6) {
                    // 현재 가지고 있는 키가 'a'일 때
                    // key : 000001;
                    // graph[nx][ny] - 'A' -> 0

                    // 현재 문의 값이 'A'라면
                    // checkDoor = 000001 = 000001 따라서, key와 문의 짝이 맞는다 라는 것을 뜻한다.
                    //              and
                    //             000001

                    // 현재 문의 값이 'A'가 아니라면
                    // checkDoor의 값은 0이 된다.
                    int checkDoor = (1 << (graph[nx][ny] - 'A')) & key;

                    // 일치하는 열쇠가 있다면
                    if (checkDoor > 0) {
                        visited[nx][ny][key] = true;
                        q.add(new Node(nx, ny, count + 1, key));
                    }
                }
                // 현재 위치가 빈 칸 '.'이라면
                else {
                   visited[nx][ny][key] = true;
                    q.add(new Node(nx, ny, count + 1, key));
                }
            }
        }

        // 모든 탐색이 끝났음에도 탈출로를 찾지 못했다면 -1 출력
        System.out.println(-1);
    }

    static class Node {
        int x;
        int y;
        int count;
        int key;

        public Node(int x, int y, int count, int key) {
            this.x = x;
            this.y = y;
            this.count = count;
            this.key = key;
        }
    }
}