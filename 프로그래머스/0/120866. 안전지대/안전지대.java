import java.util.*;
class Solution {
    static int[] dx = new int[] {-1, -1, -1, 0, 1, 1, 1, 0};
    static int[] dy = new int[] {-1, 0, 1, 1, 1, 0, -1, -1};
    static int N;
    public int solution(int[][] board) {
        N = board.length;
        int result = 0;
        for (int x = 0; x < board.length; x++ ){
            for (int y = 0; y < board[x].length; y++) {
                if (board[x][y] != 1) continue;
                marking(x, y, board);
            }
        }
        
        for (int i = 0; i < N; i++) {
            result += Arrays.stream(board[i])
                .filter(it -> it == 0)
                .count();
        }
        
        return result;
    }
    
    public void marking(int x, int y, int[][] board) {
        for (int i = 0; i < 8; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            
            if (outOfRange(nx, ny)) continue;
            if (board[nx][ny] == 1) continue;
            
            board[nx][ny] = 2;
        }
    }
    
    public boolean outOfRange(int x, int y) {
        return x < 0 || y < 0 || x >= N || y >= N;
    }
}