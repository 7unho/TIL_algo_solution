import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_17471_게리맨더링 {
    static int N;
    static int[] persons;
    static boolean[] visited;
    static List<int[]> graph;
    static List[] area;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        persons = new int[N];
        visited = new boolean[N];
        graph = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            persons[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[] node = new int[n];

            for (int j = 0; j < n; j++) {
                node[j] = Integer.parseInt(st.nextToken());
            }

            graph.add(node);
        }


        // 조합 변수 -> [], []
        // ex) combi -> [1], [2, 3, 4, 5, 6]
        for (int i = 1; i <= N / 2 ; i++) {
            combi(0, i);
            bfs();
        }


    }

    static void combi(int start, int r){
        if(r == 0){
            List<Integer> area_1 = new ArrayList<>();
            List<Integer> area_2 = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                if(visited[i]) area_1.add(i);
                else area_2.add(i);
            }

            area = new List[]{area_1, area_2};
            return;
        }

        for (int i = start; i < N; i++) {
            visited[i] = true;
            combi(i + 1, r - 1);
            visited[i] = false;
        }
    }

    static void bfs(List[] area){
        Queue<Integer> queue = new LinkedList<>();

    }
}


// Solution
// 2개의 구역으로 나누는 모든 경우의 수를 찾으면서..
// 1, 2, 3, 4, 5, 6
// nC1 + nC2 + nC3 -> 의 경우의 수.

// 선거구는
// 1. 구역을 적어도 하나 포함해야 한다.
// 2. 한 선거구에 포함되어 있는 구역은 모두 연결되어야 한다.
// area_1 = [1, 2]
// area_2 = [3, 4, 5, 6]

// 인구차의 최소를 구해라.