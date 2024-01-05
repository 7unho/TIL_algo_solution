package SWEA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Solution_삼각김밥 {
    public static Node start, end;
    public static int[] dx = {-1, -1, 0, 1, 1, 0};
    public static int[] dy = {-1, 0, 1, 1, 0, -1};
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine());
        int S, E;
        for (int tc = 1; tc <= TC; tc++) {
            st = new StringTokenizer(br.readLine());
            S = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());

            // visited 배열 초기화
            int[][] visited = new int[142][142];
            for(int i = 0; i <= 141; i++){
                Arrays.fill(visited[i], -1);
            }

            setPoints(S, E);
            System.out.printf("#%d %d\n", tc, solution(visited));
        }
    }

    private static int solution(int[][] visited) {
        if(start.x == end.x && start.y == end.y) return 0;

        int dist = 0;
        Queue<Node> q = new LinkedList<>();
        q.add(start);

        while(!q.isEmpty()){
            Node current = q.poll();

            if(current.x == end.x && current.y == end.y) {
                dist = current.dist;
                break;
            }

            for(int i = 0; i < 6; i++){
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if(pointIsInValid(nx, ny)) continue;
                if(visited[nx][ny] >= 0) continue;
                visited[nx][ny] = current.dist + 1;
                q.add(new Node(nx, ny, current.dist + 1));
            }
        }

        return dist;
    }

    private static boolean pointIsInValid(int nx, int ny) {
        return nx < 0 || ny < 0 || nx >= 142 || ny >= 142;
    }

    private static void setPoints(int s, int e) {
        int val = 1;

        for(int i = 0; i < 142; i++){
            for(int j = 0; j < 142; j++){
                if(i < j) continue;
                if(val > 10000) continue;
                if(val == s) start = new Node(i, j, 0);
                if(val == e) end = new Node(i, j, -1);
                val += 1;
            }
        }
    }

    static class Node{
        public int x;
        public int y;
        public int dist;

        public Node() {}

        public Node(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "x=" + x +
                    ", y=" + y +
                    ", dist=" + dist +
                    '}';
        }
    }
}