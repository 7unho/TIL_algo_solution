
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    // 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
    // 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
    // |r1 - r2| + |c1 - c2|

    // 0 : 빈칸, 1 : 집, 2 : 치킨집
    static int N, M, answer = 0;
    static List<int[]> targetList, homeList;
    static int[][] graph;
    static boolean[] isSelected;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N][N];
        targetList = new ArrayList<int[]>();
        homeList = new ArrayList<>();
        answer = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 2) targetList.add(new int[]{i, j});
                if (graph[i][j] == 1) homeList.add(new int[]{i, j});
            }
        }
        isSelected = new boolean[targetList.size()];
        makeList(0, 0);
        System.out.println(answer);
    }

    public static void makeList(int depth, int cnt) {
        if (depth >= targetList.size()) {
            if (cnt == M) {
                int sum = 0;
                for (int i = 0; i < homeList.size(); i++) {
                    int temp = Integer.MAX_VALUE;
                    for (int j = 0; j < targetList.size(); j++) {
                        if(!isSelected[j]) continue;

                        temp = Math.min(temp,
                                Math.abs(homeList.get(i)[0] - targetList.get(j)[0]) +
                                Math.abs(homeList.get(i)[1] - targetList.get(j)[1]));
                    }
                    sum += temp;
                }
                answer = Math.min(answer, sum);
            }
            return;
        }

        isSelected[depth] = true;
        makeList(depth + 1, cnt + 1);
        isSelected[depth] = false;
        makeList(depth + 1, cnt);
    }

}
