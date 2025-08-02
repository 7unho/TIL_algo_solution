import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Long answer = 0L;
        Long T = Long.parseLong(st.nextToken());

        Map<Long, Long> aCountMap = buildCountMap(br, st);
        Map<Long, Long> bCountMap = buildCountMap(br, st);

        for (Map.Entry<Long, Long> entry: aCountMap.entrySet()) {
            long condition = T - entry.getKey();
            if (!bCountMap.containsKey(condition)) continue;

            answer += entry.getValue() * bCountMap.get(condition);
        }

        System.out.println(answer);
    }

    private static Map<Long, Long> buildCountMap(BufferedReader br, StringTokenizer st) throws IOException {
        Map<Long, Long> result = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        long[] numbers = new long[m];
        long[][] dp = new long[m][m];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < m; i++) {
            long number = Long.parseLong(st.nextToken());
            numbers[i] = number;
            dp[i][i] = number;
            result.merge(number, 1L, Long::sum);
        }

        for (int i = 0; i < m - 1; i++) {
            for (int j = i + 1; j < m; j++) {
                long sum = dp[i][j - 1] + dp[j][j];
                dp[i][j] = sum;
                result.merge(sum, 1L, Long::sum);
            }
        }

        return result;
    }
}