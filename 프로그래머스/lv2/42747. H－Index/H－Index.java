/*
    citations: i번째 논문의 인용 횟수
    return: H의 최댓값
    
    N : 5
    0, 
*/

import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);
        for(int i = citations.length; i >= 1; i--){
            if(!isValid(citations, i)) continue;
            answer = i;
            break;
        }
        return answer;
    }
    
    // h값이 될 수 있는지
    public boolean isValid(int[] citations, int index){
        int hCnt = 0;
        int rCnt = 0;
        for(int i = 0; i < citations.length; i++){
            if(citations[i] >= index) hCnt += 1;
            else if(citations[i] <= index) rCnt += 1;
        }
        
        return (hCnt >= index && rCnt <= index) ? true: false;
    }
}