import java.util.*;
// 각 단어의 짝수: 대문자
//         홀수: 소문자

// 공백일 경우 그대로 해주되, 공백 다음 문자는 무조건 대문자이므로 flag = 짝수로 변경
// 캐릭터일 경우, 플래그 값에 따라 대소문자 변환
class Solution {
    public char converter(char c, boolean isOdd){
        return isOdd ? Character.toUpperCase(c) : Character.toLowerCase(c);
    }
    public String solution(String s){
        StringBuilder builder = new StringBuilder();
        boolean isOdd = true;
        for(char c: s.toCharArray()){
            if(!Character.isAlphabetic(c)) {
                builder.append(c);
                isOdd = true;
                continue;
            }
            builder.append(converter(c, isOdd));
            isOdd = !isOdd;
        }
        return builder.toString();
    }
}
// 1. split 이용 
// === > 공백에서 예외 처리 안됨
// class Solution {
//     public String wordMaker(char[] word){
//         for(int i = 0; i < word.length; i++){
//             // 짝수라면 대문자
//             if(i % 2 == 0){
//                 word[i] = Character.toUpperCase(word[i]);
//             } else {
//                 word[i] = Character.toLowerCase(word[i]);
//             }
//         }
//         return new String(word);
//     }
//     public String solution(String s) {
//         String[] words = s.split(" ");
//         StringBuilder builder = new StringBuilder();
//         for(int i = 0; i < words.length; i++){
//             builder.append(wordMaker(words[i].toCharArray()));
//             if(i == words.length - 1) continue;
//             builder.append(" ");
//         }
//         return builder.toString();
//     }
// }