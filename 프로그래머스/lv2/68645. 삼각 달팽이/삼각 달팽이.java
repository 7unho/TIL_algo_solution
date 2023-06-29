import java.util.*;

class Solution {
    private static final int[] dx = {1, 0, -1};
    private static final int[] dy = {0, 1, -1};
    
    public int[] solution(int n) {
        List<Integer> answer = new ArrayList<>();
        int num = 2;
        int x = 0;
        int y = 0;
        
        int[][] arr = new int[n][n];
        arr[0][0] = 1;
        
        for(int i = 0; i < n; i++){
            int direction = i % 3;
            
            while(true){
                int nx = x + dx[direction];
                int ny = y + dy[direction];
                
                if(nx < 0 || nx >= n || ny < 0 || ny > nx) break;
                if(arr[nx][ny] != 0) break;
                
                arr[nx][ny] = num++;
                x = nx;
                y = ny;
            }
        }
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j <= i; j++){
                answer.add(arr[i][j]);
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}