/*
board := 게임판
'.':빈공간, 'R':로봇, 'D':장애물, 'G':Goal
result := 말이 목표위치까지 도달할 수 있는 최소 이동 횟수 없다면 -1
*/


import java.util.*;

class Solution {
    static int N, M;
    // 0, 1, 2, 3 -> 상, 우, 하, 좌
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    public int solution(String[] board) {
        int answer = -1;
        N = board.length;
        M = board[0].length();
        Queue<int[]> q = new LinkedList<>();
        int[][] visited = new int[N][M];
        int sx = 0;
        int sy = 0;
        
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(board[i].charAt(j) != 'R') continue;
                sx = i;
                sy = j;
            }
        }

        q.add(new int[] {sx, sy, 0});
        
        while(!q.isEmpty()){
            int[] cur = q.poll();
            
            if(board[cur[0]].charAt(cur[1]) == 'G') {
                answer = visited[cur[0]][cur[1]];
                break;
            }
            
            for(int dir = 0; dir < 4; dir++){
                int[] next = move(dir, cur, board);
                int nx = next[0];
                int ny = next[1];
                
                if(visited[nx][ny] > 0) continue;
                visited[nx][ny] = cur[2] + 1;
                
                q.add(new int[]{nx, ny, cur[2] + 1});
            }
        }
        return answer;
    }
    
    static int[] move(int dir, int[] point, String[] board){
        int x = point[0];
        int y = point[1];
        
        while(true){
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            
            if(pointIsNotValid(nx, ny)) break;
            if(board[nx].charAt(ny) == 'D') break;
            x = nx;
            y = ny;
        }
        return new int[]{x, y};
    }
    
    static boolean pointIsNotValid(int x, int y){
        return x < 0 || y < 0 || x >= N || y >= M;
    }
}