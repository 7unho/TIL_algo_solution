import java.util.*;
/**
k := 피로도
dungeons := [필요 피로도, 소모 필요도]
*/
class Solution {
    static int N, answer;
    public int solution(int k, int[][] dungeons) {
        answer = 0;
        N = dungeons.length;
        boolean[] visited = new boolean[N];
        dfs(0, dungeons, visited, k);
        return answer;
    }
    
    static void dfs(int cnt, int[][] dungeons, boolean[] visited, int HP) {
        if (cnt > answer) answer = cnt;
        
        for(int i = 0; i < N; i++){
            if(!visited[i] && HP >= dungeons[i][0]){
                visited[i] = true;
                dfs(cnt + 1, dungeons, visited, HP - dungeons[i][1]);
                visited[i] = false;
            }
        }
    }
}