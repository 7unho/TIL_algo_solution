import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Map<Integer, List<Bridge>> graph = new HashMap<>();
        Comparator<Island> limitComparator = Comparator.comparingInt(Island::getLimit).reversed();
        Queue<Island> q = new PriorityQueue<>(limitComparator);

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] dist = new int[N];

        for (int i = 0; i < N; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken()) - 1;
            int to = Integer.parseInt(st.nextToken()) - 1;
            int limit = Integer.parseInt(st.nextToken());

            graph.computeIfAbsent(from, k -> new ArrayList<>()).add(new Bridge(from, to, limit));
            graph.computeIfAbsent(to, k -> new ArrayList<>()).add(new Bridge(to, from, limit));
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken()) - 1;
        int target = Integer.parseInt(st.nextToken()) - 1;

        q.offer(new Island(start, Integer.MAX_VALUE));
        dist[start] = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            Island current = q.poll();

            if (current.name == target) {
                break;
            }

            for (Bridge bridge: graph.get(current.name)) {
                int possibleWeight = Math.min(current.limit, bridge.weight);
                if (dist[bridge.to] >= possibleWeight) continue;
                dist[bridge.to] = possibleWeight;
                q.offer(new Island(bridge.to, possibleWeight));
            }
        }

        System.out.println(dist[target]);
    }

    static class Island {
        int name;
        int limit;

        public Island(int name, int limit) {
            this.name = name;
            this.limit = limit;
        }

        public int getLimit() {
            return this.limit;
        }
    }

    static class Bridge {
        int from;
        int to;
        int weight;

        public Bridge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
    }
}