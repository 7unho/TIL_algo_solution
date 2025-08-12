import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        Queue<Node> q = new LinkedList<>();

        int N = Integer.parseInt(tokenizer.nextToken());
        int M = Integer.parseInt(tokenizer.nextToken());
        int[][] graph = new int[N][M];
        int[][] answer = new int[N][M];
        Node start = new Node(0, 0, 0);

        int[] dx = new int[] {0, 0, 1, -1};
        int[] dy = new int[] {1, -1, 0, 0};

        for (int i = 0; i < N; i++) {
            tokenizer = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(tokenizer.nextToken());
                answer[i][j] = -1;
                if (graph[i][j] == 2) {
                   start.x = i;
                   start.y = j;
                   answer[i][j] = 0;
                }
            }
        }

        q.add(start);

        while (!q.isEmpty()) {
            Node current = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                if (graph[nx][ny] == 0) continue;
                if (answer[nx][ny] != -1) continue;
                answer[nx][ny] = current.dist + 1;
                q.offer(new Node(nx, ny, current.dist + 1));
            }
        }


        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(answer[i][j] == -1 && graph[i][j] == 0 ? 0 : answer[i][j]).append(' ');
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }

    static class Node {
        int x;
        int y;
        int dist;

        public Node(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
}