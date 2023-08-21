// 그래프 4분할 탐색
// 모두 같은 수일 경우 해당 수로 압축
// return: {0의 개수, 1의 개수}

class Solution {
    public static int[] answer = new int[]{0, 0};
    public int[] solution(int[][] arr) {
        quadPress(0, 0, arr.length, arr);
        return answer;
    }

    public void quadPress(int x, int y, int size, int[][] arr){
        int h = size / 2;
        // 종료조건
        // 해당 범위의 숫자가 모두 같다면, 해당 숫자 += 1        
        int condition = isValid(x, y, size, arr);
        if(condition != -1) {
            answer[condition] += 1;
            return;
        }
        
        // 2사분면
        quadPress(x, y, h, arr);
        
        // 1사분면
        quadPress(x, y + h, h, arr);
        
        // 3사분면
        quadPress(x + h, y, h, arr);
        
        // 4사분면
        quadPress(x + h, y + h, h, arr);
    }
    
    // 범위 검사 메서드
    // 모두 1로 같다면 return 1
    // 모두 0으로 같다면 return 0
    // 같지 않다면, return -1
    public int isValid(int x, int y, int size, int[][] arr){
        int condition = arr[x][y];
        
        for(int i = x; i < size + x; i++){
            for(int j = y; j < size + y; j++){
                if(condition != arr[i][j]) return -1;
            }
        }
        
        return condition;
    }
}