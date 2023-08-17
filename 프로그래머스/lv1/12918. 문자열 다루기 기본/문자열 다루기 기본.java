class Solution {
    public boolean solution(String s) {
        // 문자열의 길이가 4, 6, 숫자로만 구성되어 있는지
        return s.matches("[0-9]{4}|[0-9]{6}");
    }
}