import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static boolean answer = false;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N];

        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 0; i < N; i++) {
            visited = new boolean[N];
            dfs(i, 0, visited);
            if(answer) break;
        }

        System.out.println((answer) ? 1 : 0);
    }

    static void dfs(int x, int cnt, boolean[] visited){
        if(cnt == 4) {
            answer = true;
            return;
        }
        visited[x] = true;
        for (int i = 0; i < graph[x].size(); i++) {
            if(!visited[graph[x].get(i)]) {
                dfs(graph[x].get(i), cnt + 1, visited);
            }
            if(answer) return;
        }
        visited[x] = false;

    }
}

