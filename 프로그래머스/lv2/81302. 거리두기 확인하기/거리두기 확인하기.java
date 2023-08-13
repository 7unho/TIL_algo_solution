import java.util.*;

// 맨해튼 거리 ( |x1 - x2| + |y1 - y2| > 2 [단, 파티션이 있다면 가능])
// 응시자(P), 빈 테이블(0), 파티션(X)
// 한 번의 4방 탐색 진행

class Solution {
    final static int[] dx = {0, 1, -1, 0};
    final static int[] dy = {1, 0, 0, -1};
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        
        for(int i = 0; i < 5; i++){
            char[][] place = new char[5][5];
            for(int j = 0; j < 5; j++){
                place[j] = places[i][j].toCharArray();
            }
            
            if(isValid(place)) answer[i] = 1;
        }
        return answer;
    }
    
    static boolean outOfRange(int x, int y){
        if(x < 0 || y < 0 || x >= 5 || y >= 5) return true;
        return false;
    }
    
    static boolean isExist(char[][] place, int x, int y, int direction, char flag){
        for(int i = 0; i < 4; i++){
            if(direction + i == 3) continue;
            
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(outOfRange(nx, ny)) continue;
            if(place[nx][ny] == 'P' && flag == 'O') return true;
        }
        return false;
    }
    
    static boolean isValid(char[][] place){
        for(int x = 0; x < 5; x++){
            for(int y = 0; y < 5; y++){
                if(place[x][y] != 'P') continue;
                
                for(int i = 0; i < 4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    
                    if(outOfRange(nx, ny)) continue;
                    
                    if(place[nx][ny] == 'P') return false;
                    if(isExist(place, nx, ny, i, place[nx][ny])) return false;
                }
            }
        }
        return true;
    }
}

