import java.util.*;
/* 
1. 모든 직선 쌍에 대해 반복
    1-1. 교점 좌표 구하기
    1-2. 정수 좌표만 저장
2. 저장된 정수들에 대해 x, y 좌표의 최댓값, 최솟값 구하기
3. 구한 최대, 최소를 통해 2차원 배열의 크기 결정
4. 2차원 배열에 별 표시
*/
class Solution {
    private static class Point {
        public final long x, y;
        private Point(long x, long y){
            this.x = x;
            this.y = y;
        }
    }
    
    // 1-1. 교점 좌표 구해서 정수 좌표만 return
    private Point intersaction(long a, long b, long e, long c, long d, long f) {
        if(a * d - b * c == 0) return null;
        
        double x = (double) (b * f - e * d) / (a * d - b * c);
        double y = (double) (e * c - a * f) / (a * d - b * c);
        
        if(x % 1 != 0 || y % 1 != 0) return null;
        
        return new Point((long) x, (long) y);
    }
    
    // 2. 저장된 정수들의 최솟값 리턴
    private Point getMinimumPoint(List<Point> points){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for(Point p: points){
            if(p.x < x) x = p.x;
            if(p.y < y) y = p.y;
        }
        
        return new Point(x, y);
    }
    // 2. 저장된 정수들의 최댓값 리턴
    private Point getMaximumPoint(List<Point> points){
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        
        for(Point p: points){
            if(p.x > x) x = p.x;
            if(p.y > y) y = p.y;
        }
        
        return new Point(x, y);
    }
    
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        
        for(int i = 0; i < line.length; i++) {
            for(int j = i + 1; j < line.length; j++) {
                Point point = intersaction(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                
                if(point == null) continue;
                // 1-2. 정수 좌표만 저장
                points.add(point);
            }
        }
        
        Point maximum = getMaximumPoint(points);
        Point minimum = getMinimumPoint(points);
        
        int width = (int) (maximum.x - minimum.x) + 1;
        int height = (int) (maximum.y - minimum.y) + 1;
        
        char[][] arr = new char[height][width];
        for(char[] row: arr) Arrays.fill(row, '.');
        
        for(Point p: points){
            int x = (int)(p.x - minimum.x);
            int y = (int)(maximum.y - p.y);
            
            arr[y][x] = '*';
        }
        
        String[] answer = new String[arr.length];
        for(int i = 0; i < answer.length; i++) answer[i] = new String(arr[i]);
        
        return answer;
    }
}