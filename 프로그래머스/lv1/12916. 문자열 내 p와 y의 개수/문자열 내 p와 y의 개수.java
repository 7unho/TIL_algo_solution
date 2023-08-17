// res = p.count == y.count ? true: false;
class Solution {
    boolean solution(String s) {
        int p = 0;
        int y = 0;
        
        for(char c: s.toCharArray()){
            if(Character.toUpperCase(c) == 'P') p += 1;
            if(Character.toUpperCase(c) == 'Y') y += 1;
        }
        return p == y ? true: false;
    }
}