import java.util.*;

class Solution {
    static int N;
    public int solution(String arr[]) {
        int answer = Integer.MIN_VALUE;
        N = arr.length / 2 + 1;
        int[] numbers = new int[N];
        String[] opers = new String[N - 1];
        
        // 숫자, 연산자 분리
        for(int i = 0; i < arr.length; i++) {
            if(i % 2 == 0) numbers[i / 2] = Integer.parseInt(arr[i]);
            else opers[i / 2] = arr[i];
        }
        
        // dp 배열 초기화
        int[][] maxDp = new int[N][N];
        int[][] minDp = new int[N][N];
        
        for(int i = 0; i < N; i++){
            Arrays.fill(maxDp[i], Integer.MIN_VALUE);
            Arrays.fill(minDp[i], Integer.MAX_VALUE);
        }
        
        for(int step = 0; step < N; step++){
            for(int i = 0; i < N - step; i++) {
                int j = i + step;
                if(i == j) {
                    maxDp[i][j] = numbers[i];
                    minDp[i][j] = numbers[i];
                    continue;
                }
                for(int k = i; k < j; k++) {
                    // 1. 연산자가 +라면,
                    if(opers[k].equals("+")) {
                        // 1-1. maxDP
                        //      dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])
                        maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] + maxDp[k + 1][j]);
                        // 1-2. minDP
                        //      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                        minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] + minDp[k + 1][j]);
                        continue;
                    }
                    // 2. 연산자가 -라면,
                    // 2-1. maxDP
                    //      dp[i][j] = max(dp[i][j], max[i][k] - min[k + 1][j])
                    maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] - minDp[k + 1][j]);
                    // 2-2. minDP
                    //      dp[i][j] = min(dp[i][j], min[i][k] - max[k + 1][j])
                    minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] - maxDp[k + 1][j]);
                }
            }
        }
        return maxDp[0][N - 1];
    }
}