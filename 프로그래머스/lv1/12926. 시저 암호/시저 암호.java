class Solution {
    public char converter(char c, int n){
        if(!Character.isAlphabetic(c)) return c;
        
        int offset = Character.isUpperCase(c) ? 'A': 'a';
        int position = c - offset;
        position = (position + n) % ('Z' - 'A' + 1);
        return (char) (offset + position);
    }
    public String solution(String s, int n) {
        StringBuilder builder = new StringBuilder();
        
        for(char c: s.toCharArray()){
            builder.append(converter(c, n));
        }
        return builder.toString();
    }
}