import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int answer = 0;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] items = new int[N];
        for (int i = 0; i < N; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(items);

        if (N <= 2) {
            System.out.println(0);
            System.exit(0);
        }

        for (int i = 0; i < N; i++) {
            int start = 0;
            int end = N - 1;
            int target = items[i];

            while (start < end) {
                if (start == i) {
                    start++;
                    continue;
                }
                if (end == i) {
                    end--;
                    continue;
                }

                int sum = items[start] + items[end];
                if (sum == target) {
                    answer++;
                    break;
                } else if (sum < target) {
                    start++;
                } else {
                    end--;
                }
            }
        }

        System.out.println(answer);
    }
}