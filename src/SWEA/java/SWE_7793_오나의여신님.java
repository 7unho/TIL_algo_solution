import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class SWE_7793_오나의여신님 {
    static int N, M;
    static int[][] dist;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine());
        int answer;
        char[][] graph;


        for (int tc = 1; tc <= TC; tc++) {
            answer = 0;

            Queue<Node> user_queue = new LinkedList<>();
            Queue<Node> virus_queue = new LinkedList<>();
            Node target = new Node();

            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            graph = new char[N][M];
            dist = new int[N][M];

            for (int i = 0; i < N; i++) {
                graph[i] = br.readLine().toCharArray();

                for (int j = 0; j < M; j++) {
                    if(graph[i][j] == 'S'){
                        user_queue.offer(new Node(i, j));
                    } else if(graph[i][j] == 'D'){
                        target.x = i;
                        target.y = j;
                    } else if(graph[i][j] == '*'){
                        virus_queue.offer(new Node(i, j));
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    dist[i][j] = -1;
                }
            }

            Node start = user_queue.peek();
            dist[start.x][start.y] = 0;

            while(!user_queue.isEmpty()){
                for (int v = 0; v < virus_queue.size(); v++) {
                    Node virus = virus_queue.poll();

                    for (int i = 0; i < 4; i++) {
                        Node nVirus = new Node(virus.x + dx[i], virus.y + dy[i]);

                        if(nVirus.x < 0 || nVirus.y < 0 || nVirus.x >= N || nVirus.y >= M) continue;

                        if(graph[nVirus.x][nVirus.y] == '.'){
                            graph[nVirus.x][nVirus.y] = '*';
                            virus_queue.offer(nVirus);
                        }
                    }
                }

                for (int u = 0; u < user_queue.size(); u++) {
                    Node user = user_queue.poll();

                    if(user.x == target.x && user.y == target.y) break;

                    for (int i = 0; i < 4; i++) {
                        Node nUser = new Node(user.x + dx[i], user.y + dy[i]);

                        if(nUser.x < 0 || nUser.y < 0 || nUser.x >= N || nUser.y >= M) continue;

                        if(graph[nUser.x][nUser.y] == 'X' || graph[nUser.x][nUser.y] == '*') continue;

                        if(dist[nUser.x][nUser.y] == -1){
                            dist[nUser.x][nUser.y] = dist[user.x][user.y] + 1;
                            user_queue.offer(nUser);
                        }
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                System.out.println(Arrays.toString(dist[i]));
            }
            if(dist[target.x][target.y] >= 0) System.out.printf("#%d %d\n", tc, dist[target.x][target.y]);
            else System.out.printf("#%d GAME OVER\n", tc);
        }
    }
}
class Node{
    public int x;
    public int y;

    public Node() {}

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
