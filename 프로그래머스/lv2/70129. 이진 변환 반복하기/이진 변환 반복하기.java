// 1. x의 모든 0을 제거
// 2. func(x) -> x의 길이를 2진법으로 표현한 문자열

// s가 1이 될 때 까지, 1-2 반복.
// answer = [1-2반복 횟수, 제거된 0의 총 개수]
class Solution {
    public String[] step1(char[] s){
        int count = 0;
        for(char c: s){
            if(c == '0') count += 1;
        }
        return new String[] {Integer.toString(s.length - count, 2), Integer.toString(count)};
    }
    public int[] solution(String s) {
        int round = 0; // 회차
        int count = 0; // 제거된 0의 총 개수
        while(true){
            if(s.equals("1")) break;
            
            // res = {변환된 문자열, 제거된 0 개수}
            String[] res = step1(s.toCharArray());
            
            s = res[0];
            count += Integer.valueOf(res[1]);
            round += 1;
        }
        return new int[] {round, count};
    }
}