import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static int N, M;
    static int[] indegree;
    static List<List<Integer>> graph;
    static List<Integer> answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        answer = new ArrayList<>();
        Queue<Integer> q = new PriorityQueue<>();

        indegree = new int[N + 1];
        graph = new ArrayList<>();

        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int prev = Integer.parseInt(st.nextToken());
            int next = Integer.parseInt(st.nextToken());

            indegree[next] += 1;
            graph.get(prev).add(next);
        }

        for (int i = 1; i <= N; i++) {
            if (indegree[i] != 0) continue;
            q.offer(i);
        }

        while (!q.isEmpty()) {
            int node = q.poll();
            answer.add(node);

            for (int nx: graph.get(node)) {
                indegree[nx] -= 1;
                if (indegree[nx] == 0) {
                    q.offer(nx);
                }
            }
        }

        for (int i = 0; i < answer.size(); i++) {
            System.out.print(answer.get(i) + " ");
        }
    }
}