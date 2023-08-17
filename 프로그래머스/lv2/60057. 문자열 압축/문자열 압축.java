import java.util.*;
// 1. 1부터 s까지 자를 문자열의 길이 설정
// 2. 설정된 길이만큼 문자열을 잘라 낸 리스트 생성
// 3. 문자열을 비교하며 리스트의 배열을 하나의 문자열로 압축
// 4. 1~3 과정으로 압축된 문자열 중 가장 짧은 길이 반환

class Solution {
    public int compress(List<String> tokens){
        StringBuilder res = new StringBuilder();
        int count = 1;
        String last = "";
        
        for(String token: tokens){
            
            // 직전 문자열과 현재 토큰값이 같다면
            if(last.equals(token)) {
                count += 1;
                continue;
            }
            
            // 직전 문자열과 현재 토큰 값이 다르다면
            // count + 토큰 값 res에 append
            if(count > 1) res.append(count);
            res.append(last);
            // last 값 변경
            last = token;
            count = 1;
        }
        if(count > 1) res.append(count);
        res.append(last);
        
        return res.length();
    }
    public int solution(String s) {
        int answer = Integer.MAX_VALUE;
        
        // 1. 1부터 s까지 자를 문자열의 길이 설정
        for(int len = 1; len <= s.length(); len++){
            List<String> tokens = new ArrayList<>();
            for(int start = 0; start < s.length(); start += len){
                int end = start + len;
                if(end >= s.length()) end = s.length();
                tokens.add(s.substring(start, end));
            }
            answer = Math.min(answer, compress(tokens));
        }
        
        return answer;
    }
}