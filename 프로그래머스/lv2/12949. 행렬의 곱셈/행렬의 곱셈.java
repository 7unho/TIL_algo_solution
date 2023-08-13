class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int rows = arr1.length;
        int cols = arr2[0].length;
        int[][] answer = new int[rows][cols];
        
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                for(int k = 0; k < arr2.length; k++){
                    answer[r][c] += arr1[r][k] * arr2[k][c];
                }
            }
        }
        return answer;
    }
}