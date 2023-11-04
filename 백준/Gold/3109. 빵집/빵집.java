import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int R, C, answer;
    static char[][] map;
    static int[] dx = { -1, 0, 1 };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new char[R][C];
        answer = 0;

        for (int i = 0; i < R; i++) {
            map[i] = br.readLine().toCharArray();
        }

        for (int i = 0; i < R; i++) {
            if(dfs(i, 0)) answer += 1;
        }

        System.out.println(answer);
        br.close();
    }

    public static boolean dfs(int x, int y){
        for (int i = 0; i < 3; i++) {
            int nx = x + dx[i];
            int ny = y + 1;

            if(nx >= 0 && nx < R && map[nx][ny] == '.'){
                if(ny == C - 1) return true;

                map[nx][ny] = 'x';
                if(dfs(nx, ny)) return true;
            }
        }
        return false;
    }
}
