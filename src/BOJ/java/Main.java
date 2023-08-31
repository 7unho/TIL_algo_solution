import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] graph;
    static StringBuilder answer;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        answer = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];

        for(int i = 0; i < N; i++){
            char[] arr = br.readLine().toCharArray();
            for(int j = 0; j < N; j++){
                graph[i][j] = arr[j] - '0';
            }
        }
        solution(0, 0, N);
//        System.out.println(answer.toString());
    }

    static void solution(int x, int y, int size){
        int h = size / 2;
        // 종료조건
        // 범위 내의 모든 숫자가 같을 때,
        if(isValid(x, y, size)){
            answer.append(graph[x][y]);
            System.out.print(graph[x][y]);
            return;
        }
        answer.append("(");
        System.out.print("(");
        solution(x, y, h);
        solution(x, y + h, h);
        solution(x + h, y, h);
        solution(x + h, y + h, h);
        answer.append(")");
    }

    static boolean isValid(int x, int y, int size){
        int condition = graph[x][y];

        for(int i = x; i < x + size; i++){
            for(int j = y; j < y + size; j++){
                if(condition != graph[i][j]) return false;
            }
        }

        return true;
    }
}
