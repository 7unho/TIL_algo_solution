import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, answer;
    static int[][] innings;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        int[] players = new int[9];
        innings = new int[N][9];
        boolean[] isSelected = new boolean[9];
        answer = 0;

        for (int i = 0; i < N ; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                innings[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        isSelected[3] = true;
        players[3] = 0;
        perm(1, isSelected, players);
        System.out.println(answer);
    }

    public static void perm(int depth, boolean[] isSelected, int[] players){
        if(depth > 8){
            answer = Math.max(answer, play(players));
            return;
        }

        for (int i = 0; i < 9; i++) {
            if(isSelected[i]) continue;
            isSelected[i] = true;
            players[i] = depth;
            perm(depth + 1, isSelected, players);
            isSelected[i] = false;
        }
    }

    public static int play(int[] players) {
        int res = 0;
        int hitter = 0;
        for(int[] inning: innings){
            int[] bases = new int[4];
            int outCnt = 0;

            while(outCnt < 3){
                switch (inning[players[hitter]]){
                    case 0:
                        outCnt += 1;
                        break;
                    case 1:
                        res += bases[3];
                        bases[3] = bases[2];
                        bases[2] = bases[1];
                        bases[1] = 1;
                        break;
                    case 2:
                        res += bases[3] + bases[2];
                        bases[3] = bases[1];
                        bases[2] = 1;
                        bases[1] = 0;
                        break;
                    case 3:
                        res += bases[3] + bases[2] + bases[1];
                        bases[3] = 1;
                        bases[2] = 0;
                        bases[1] = 0;
                        break;
                    case 4:
                        res += bases[3] + bases[2] + bases[1] + 1;
                        bases[3] = 0;
                        bases[2] = 0;
                        bases[1] = 0;
                        break;
                }

                hitter = (hitter + 1) % 9;
            }
        }

        return res;
    }
}
