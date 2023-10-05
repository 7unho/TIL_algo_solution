class Solution {
    public int solution(int n) {
        int[] answers = new int[n + 1];
        answers[1] = 1;
        answers[2] = 1;
        
        for(int i=3; i<=n; i++){
            answers[i] = (answers[i - 2] + answers[i - 1]) % 1234567;
        }
        return answers[n];
    }
}