import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWE_8458_원점으로 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            int N = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int max_points = cal(x, y);
            int isOdd = (max_points % 2 == 1) ? 1 : 0;

            for (int i = 1; i < N; i++) {
                st = new StringTokenizer(br.readLine());

                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());

                int temp = cal(x,  y);
                if(isOdd != (temp % 2)){
                    max_points = -1;
                    for (int j = i + 1; j < N; j++) br.readLine();
                    break;
                }

                max_points = Math.max(max_points, temp);
            }

            if(max_points == -1){
                System.out.printf("#%d -1\n", tc);
                continue;
            }

            int answer = 0;

            while(max_points > 0){
                answer += 1;
                max_points -= answer;
            }

            max_points *= -1;

            if(max_points % 2 == 1){
                answer = (max_points % 2 == 0) ? answer + 1 : answer + 2;
            }
            System.out.printf("#%d %d\n", tc, answer);
        }

    }

    public static int cal(int x, int y){
        return Math.abs(x) + Math.abs(y);
    }
}
