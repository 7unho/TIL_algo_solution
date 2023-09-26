import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int R, C, T, answer;
    static int[][] map, temp;
    static int[] airs = new int[2];

    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        answer = 0;

        map = new int[R][C];

        int idx = 0;
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == -1) airs[idx++] = i;
            }
        }

        for (int i = 0; i < T; i++) {
            temp = new int[R][C];
            temp[airs[0]][0] = -1;
            temp[airs[1]][0] = -1;

            Solution1();
            Solution2();

        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if(map[i][j] >= 0) answer += map[i][j];
            }
        }

        System.out.println(answer);
    }

    // 구현 1, 전체 미세먼지 확산 먼저 하면서. 확산 누적값 저장
    static void Solution1(){
        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                if(map[x][y] == -1) continue;

                int sum = 0;
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if(nx >= 0 && nx < R && ny >= 0 && ny < C && map[nx][ny] >= 0){
                        temp[nx][ny] += map[x][y] / 5;
                        sum += map[x][y] / 5;
                    }
                }
                temp[x][y] += map[x][y] - sum;
            }
        }

        map = temp;
    }

    // 구현 2, 바람 순회
    static void Solution2(){
        // 반시계 방향
        for (int x = airs[0] - 1; x > 0; x--) {
            map[x][0] = map[x - 1][0];
        }

        for (int y = 0; y < C - 1; y++) {
            map[0][y] = map[0][y + 1];
        }

        for (int x = 0; x < airs[0]; x++) {
            map[x][C - 1] = map[x + 1][C - 1];
        }

        for (int y = C - 1; y > 1; y--) {
            map[airs[0]][y] = map[airs[0]][y - 1];
        }

        map[airs[0]][1] = 0;

        // 시계 방향
        for (int x = airs[1] + 1; x < R - 1; x++) {
            map[x][0] = map[x + 1][0];
        }

        for (int y = 0; y < C - 1; y++) {
            map[R - 1][y] = map[R - 1][y + 1];
        }

        for (int x = R - 1; x > airs[1]; x--) {
            map[x][C - 1] = map[x - 1][C - 1];
        }

        for (int y = C - 1; y > 1; y--) {
            map[airs[1]][y] = map[airs[1]][y - 1];
        }

        map[airs[1]][1] = 0;
    }
}
