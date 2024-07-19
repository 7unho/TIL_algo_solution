import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] choices = new int[d + 1];

        int[] graph = new int[N + k - 1];

        for (int i = 0; i < N; i++) {
            graph[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < k - 1; i++) {
            graph[N + i] = graph[i];
        }

        int start = 0;
        choices[c] = 1;
        int cnt = 1;
        int answer = 1;
        int window = 0;

        for (int end = 0; end < graph.length; end++) {
            window += 1;
            choices[graph[end]] += 1;
            cnt = (choices[graph[end]] == 1) ? cnt + 1 : cnt;

            if(window > k){
                window -= 1;
                choices[graph[start]] -= 1;
                cnt = (choices[graph[start]] == 0) ? cnt - 1 : cnt;
                start += 1;
            }

            answer = Math.max(answer, cnt);
        }

        System.out.println(answer);
    }
}
