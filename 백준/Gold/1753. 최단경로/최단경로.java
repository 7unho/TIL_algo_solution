import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

/**
 * answer = [K번 노드부터 i번 노드까지의 최단 거리]
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Map<Integer, List<Edge>> graph = new HashMap<>();
        Comparator<Node> sumComparator = Comparator.comparingInt(Node::getSum);
        Queue<Node> q = new PriorityQueue<>(sumComparator);

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        // K에서 i까지의 최단거리
        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);

        st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken()) - 1;

        for (int i = 0; i < V; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken()) - 1;
            int to = Integer.parseInt(st.nextToken()) - 1;
            int weight = Integer.parseInt(st.nextToken());

            graph.computeIfAbsent(from, v -> new ArrayList<>()).add(new Edge(from, to, weight));
        }

        dist[K] = 0;
        q.offer(new Node(K, 0));

        while (!q.isEmpty()) {
            Node current = q.poll();

            for (Edge edge: graph.get(current.id)) {
                if (dist[edge.to] <= current.sum + edge.weight) continue;
                dist[edge.to] = current.sum + edge.weight;
                q.offer(new Node(edge.to, dist[edge.to]));
            }
        }

        IntStream.range(0, V)
                .mapToObj(i -> dist[i] == Integer.MAX_VALUE ? "INF" : dist[i])
                .forEach(System.out::println);
    }

    static class Node {
        int id;
        int sum;

        public Node(int id, int sum) {
            this.id = id;
            this.sum = sum;
        }

        public int getSum() {
            return this.sum;
        }
    }
    static class Edge {
        int from;
        int to;
        int weight;

        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
    }
}