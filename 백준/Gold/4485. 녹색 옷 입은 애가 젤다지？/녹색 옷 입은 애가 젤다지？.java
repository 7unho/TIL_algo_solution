import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int TC = 1;
        while (true) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            if (N == 0) break;

            int[][] graph = new int[N][N];
            int[][] dp = new int[N][N];
            boolean[][] visited = new boolean[N][N];
            Comparator<Node> comparator = Comparator.comparingInt(Node::getWeight);
            Queue<Node> q = new PriorityQueue<>(comparator);

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                Arrays.fill(dp[i], Integer.MAX_VALUE);

                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            dp[0][0] = graph[0][0];

            Node start = new Node(0, 0, graph[0][0]);
            q.offer(start);

            while (!q.isEmpty()) {
                Node current = q.poll();
                visited[current.x][current.y] = true;

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                    if (dp[current.x][current.y] + graph[nx][ny] >= dp[nx][ny]) continue;
                    dp[nx][ny] = dp[current.x][current.y] + graph[nx][ny];
                    q.offer(new Node(nx, ny, dp[current.x][current.y] + graph[nx][ny]));
                }
            }

            System.out.printf("Problem %s: %s\n", TC, dp[N - 1][N - 1]);
            TC += 1;
        }
    }

    static class Node {
        int x;
        int y;
        int weight;

        public Node(int x, int y, int weight) {
            this.x = x;
            this.y = y;
            this.weight = weight;
        }

        public int getWeight() {
            return this.weight;
        }
    }
}